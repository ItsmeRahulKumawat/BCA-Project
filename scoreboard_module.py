import pygame.font
from pygame.sprite import Group
from rocket_module import Rocket

class ScoreBoard():
    """A class to report scoring information"""
    def __init__(self, setting_obj, screen, stat_obj):
        """Initialize scorekeeping attribute"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.setting_obj = setting_obj
        self.stats = stat_obj

        # font setting for storing information
        self.text_color = (100,100,100)
        self.font = pygame.font.SysFont(None, 60)

        # prepare the initial score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_rockets()

    def prep_score(self):
        """Turn the score into the render image"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render("Score- "+score_str, True, self.text_color, self.setting_obj.trans)

        # display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turns the high score into a render image"""
        high_score_str = str(self.stats.high_score)
        self.high_score_image = self.font.render("High Score- "+high_score_str, True, self.text_color, self.setting_obj.trans)

        # display the gigh score at middle top screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Turn the level into a rendered image."""
        self.level_image = self.font.render("Lvl- "+str(self.stats.level), True, self.text_color, self.setting_obj.trans)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_rockets(self):
        """Show how many rockets are left."""
        self.rockets = Group()
        for rocket_number in range(self.stats.rockets_left):
            rocket = Rocket(self.setting_obj, self.screen)
            rocket.rect.x = 10 + rocket_number * rocket.rect.width
            rocket.rect.y = 10
            self.rockets.add(rocket)

    def show_score(self):
        """Draw the score to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # draw rockets
        self.rockets.draw(self.screen)