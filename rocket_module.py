# rocket.py

import pygame
from pygame.sprite import Sprite

class Rocket(Sprite):
    def __init__(self, setting_obj, screen):
        """Initialize rocket at starting position"""
        super().__init__()
        self.screen = screen
        self.setting_obj = setting_obj
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the rocket's center.
        self.center = float(self.rect.centerx)

        # movement flags
        self.moving_right = False
        self.moving_left = False

    """Updates rocket when key is pressed whether left or right based on movement flags"""
    def update(self):
        # Update the rocket's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.setting_obj.rocket_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.setting_obj.rocket_speed_factor

        # Update rect object from self.center.
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the rocket at its current location"""
        self.screen.blit(self.image,self.rect)

    def center_rocket(self):
        """Center the rocket on the screen."""
        self.center = self.screen_rect.centerx

