# game_functions.py

import sys
import pygame
from bullet_module import Bullet
from alien_module import Alien
from time import sleep



def check_keydown_evnets(event, stat_obj, setting_obj, screen, rocket, bullet_inst):
    """This part works when any kinds of user input is given through keyboard"""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = True
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(setting_obj,screen,rocket,bullet_inst)
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_p:
        stat_obj.game_active = True


def check_keyup_events(event, rocket):
    """This part works key is released"""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = False

def check_events(setting_obj, screen, stat_obj, scoreboard_obj, play_btn, alien_inst, rocket, bullet_inst):
    """This part works when any event occurs"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_evnets(event, stat_obj, setting_obj, screen, rocket, bullet_inst)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,rocket)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(setting_obj, screen, play_btn, stat_obj, scoreboard_obj, rocket, alien_inst, bullet_inst, mouse_x, mouse_y)

def check_play_button(setting_obj, screen, play_btn, stat_obj, scoreboard_obj, rocket, alien_inst, bullet_inst, mouse_x, mouse_y):
    """Start a new game when the player clicks Play."""
    button_clicked = play_btn.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stat_obj.game_active:
        # Reset the game settings.
        setting_obj.initialize_dynamic_settings()
        # hide the mouse cursor
        pygame.mouse.set_visible(False)
        stat_obj.reset_stats()
        stat_obj.game_active = True

        # reset the scoreboard images
        scoreboard_obj.prep_score()
        scoreboard_obj.prep_high_score()
        scoreboard_obj.prep_level()
        scoreboard_obj.prep_rockets()

        # Empty bullets and aliens list
        alien_inst.empty()
        bullet_inst.empty()

        # create a new fleet and center the rocket
        create_fleet(setting_obj, screen, rocket, alien_inst)
        rocket.center_rocket()

def update_bullets(setting_obj, screen, stat_obj, scoreboard_obj, rocket, alien_inst, bullet_inst):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    for bullet in bullet_inst.copy():
        if bullet.rect.bottom <= 0:
            bullet_inst.remove(bullet)
    check_bullet_alien_collisions(setting_obj,screen, stat_obj, scoreboard_obj, rocket, alien_inst, bullet_inst)

def check_bullet_alien_collisions(setting_obj,screen, stat_obj, scoreboard_obj, rocket, alien_inst, bullet_inst):
    """Respond to bullet-alien collisions."""
    # Remove any bullets and aliens that have collided.
    collisions = pygame.sprite.groupcollide(bullet_inst, alien_inst, True, True)
    # Check any bullets that have hit aliens.
    if collisions:
        for alien_inst in collisions.values():
            stat_obj.score += setting_obj.alien_points * len(alien_inst)
            scoreboard_obj.prep_score()
            check_high_score(stat_obj, scoreboard_obj)
    # If so, get rid of the bullet and the alien.
    if len(alien_inst) == 0:
        # if the entire fleet is destroyed
        # Destroy existing bullets, speed up game, and create new fleet.
        bullet_inst.empty()
        setting_obj.increase_speed()
        # increase level
        stat_obj.level += 1
        scoreboard_obj.prep_level()
        create_fleet(setting_obj,screen,rocket,alien_inst)


def fire_bullet(setting_obj, screen, rocket, bullet_inst):
    # checks whether max bullets on screen are 3 and adds new bullet
    if len(bullet_inst) < setting_obj.bullets_allowed:
        new_bullet = Bullet(setting_obj, screen, rocket)
        bullet_inst.add(new_bullet)

def get_number_aliens_x(setting_obj, alien_width):
    # Create an alien and find the number of aliens in a row.
    # Spacing between each alien is equal to one alien width.
    available_space_x = setting_obj.screenwidth - (2 * alien_width)
    number_alien_x = int(available_space_x / (2 * alien_width))
    return number_alien_x

def get_number_rows(setting_obj, rocket_height,  alien_height):
    """Determine the number of the row aliens that will fit on screen"""
    available_space_y = (setting_obj.screenheight - (2 * alien_height) - rocket_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(setting_obj, screen , alien_inst, alien_number, row_number):
    # Create an alien and place it in a row
    alien = Alien(setting_obj, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien_inst.add(alien)

def create_fleet(setting_obj, screen, rocket, alien_inst):
    """Create a full fleet of aliens."""
    # Create an alien and find the number of aliens in a row.
    alien = Alien(setting_obj, screen)
    number_aliens_x = get_number_aliens_x(setting_obj, alien.rect.width)
    number_rows = get_number_rows(setting_obj, rocket.rect.height, alien.rect.height)

    # Create the first row of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(setting_obj, screen, alien_inst, alien_number,
                         row_number)


"""updates the screen"""
def update_screen(setting_obj,screen,stat_obj,scoreboard_obj,rocket,alien_inst,bullet_inst,play_btn):
    # redraw the screen during each pass of the loop
    screen.fill(setting_obj.bg_color)
    # Redraw all bullets behind rocket and aliens.
    for bullet in bullet_inst.sprites():
        bullet.draw_bullet()

    rocket.blitme()
    alien_inst.draw(screen)
    # draw the scoreboard to screen
    scoreboard_obj.show_score()
    # Draw the play button if the game is inactive.
    if not stat_obj.game_active:
        play_btn.draw_button()

    # Make the most recently drawn screen visible.
    pygame.display.flip()

def check_fleet_edges(setting_obj, alien_inst):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in alien_inst.sprites():
        if alien.check_edges():
            change_fleet_direction(setting_obj, alien_inst)
            break

def change_fleet_direction(setting_obj, alien_inst):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in alien_inst.sprites():
        alien.rect.y += setting_obj.fleet_drop_speed
    setting_obj.fleet_direction *= -1

def rocket_hit(setting_obj, stat_obj, screen, scoreboard_obj, rocket, alien_inst, bullet_inst):
    """Respond to rocket being hit by alien."""
    if stat_obj.rockets_left > 0:
        # Decrement rockets_left.
        stat_obj.rockets_left -= 1

        # Update scoreboard
        scoreboard_obj.prep_rockets()

        # empty the list of bullets and aliens
        alien_inst.empty()
        bullet_inst.empty()

        # create new fleet and center the rocket
        create_fleet(setting_obj,screen,rocket,alien_inst)
        rocket.center_rocket()

        # pause
        sleep(0.5)
    else:
        stat_obj.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(setting_obj, stat_obj, screen, rocket, alien_inst, bullet_inst):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in alien_inst.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the rocket got hit.
            rocket_hit(setting_obj, stat_obj, screen, rocket, alien_inst, bullet_inst)
            break

def update_aliens(setting_obj, stat_obj, screen, scoreboard_obj, rocket, alien_inst, bullet_inst):
    """
    Check if the fleet is at an edge,
    and then update the postions of all aliens in the fleet.
    """
    check_fleet_edges(setting_obj, alien_inst)
    
    # Look for aliens hitting the bottom of the screen.
    check_aliens_bottom(setting_obj, stat_obj, screen, rocket, alien_inst, bullet_inst)
    alien_inst.update()

    # looks for collisions of rocket and aliens
    if pygame.sprite.spritecollideany(rocket, alien_inst):
        rocket_hit(setting_obj, stat_obj, screen, scoreboard_obj, rocket, alien_inst, bullet_inst)

def check_high_score(stat_obj, scoreboard_obj):
    """Check to see if there's a new high score."""
    if stat_obj.score > stat_obj.high_score:
        stat_obj.high_score = stat_obj.score
        scoreboard_obj.prep_high_score()






