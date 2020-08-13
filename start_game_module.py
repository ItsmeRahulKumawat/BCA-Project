# start_game.py

import pygame
from settings_module import Settings
from rocket_module import Rocket
import game_functions_module as gf
from pygame.sprite import Group
from game_stats_module import Game_Stats
from button_module import Button
from scoreboard_module import ScoreBoard

def run_game():
    pygame.init()
    setting_obj = Settings()

    screen = pygame.display.set_mode((setting_obj.screenwidth,setting_obj.screenheight))
    pygame.display.set_caption("Alien Forces")

    # Make a rocket, a group of bullets, and a group of aliens.
    rocket = Rocket(setting_obj, screen)

    # Create an instance to store game statistics and create a scoreboard.
    stat_obj = Game_Stats(setting_obj)
    scoreboard_obj = ScoreBoard(setting_obj, screen, stat_obj)
    # Make the Play button.
    play_btn = Button(screen,"Click To Play")


    # Make a group to store bullets in.
    bullet_inst = Group()
    alien_inst = Group()
    # Create a fleet of aliens
    gf.create_fleet(setting_obj,screen,rocket,alien_inst)

    while True:
        gf.check_events(setting_obj, screen, stat_obj, scoreboard_obj, play_btn, alien_inst, rocket, bullet_inst)
        if stat_obj.game_active:
            rocket.update()
            bullet_inst.update()
            gf.update_bullets(setting_obj,screen, stat_obj, scoreboard_obj, rocket, alien_inst, bullet_inst)
            gf.update_aliens(setting_obj, stat_obj, screen,scoreboard_obj, rocket, alien_inst, bullet_inst)
        gf.update_screen(setting_obj, screen, stat_obj, scoreboard_obj, rocket, alien_inst, bullet_inst, play_btn)

run_game()