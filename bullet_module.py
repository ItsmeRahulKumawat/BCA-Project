# bullet.py

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """a class to manage bullets fired from the rocket"""
    def __init__(self, setting_obj, screen, rocket):
        # create a bullet object from rocket current position
        super(Bullet, self).__init__()
        self.screen = screen

        # create a bullet
        self.rect = pygame.Rect(0,0,setting_obj.bullet_width,setting_obj.bullet_height)
        self.rect.centerx = rocket.rect.centerx
        self.rect.top = rocket.rect.top

        # stores bullets position as a decimal
        self.y = float(self.rect.y)

        self.color = setting_obj.bullet_color
        self.speed_factor = setting_obj.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.speed_factor
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullets to the screen"""
        pygame.draw.rect(self.screen,self.color,self.rect)
