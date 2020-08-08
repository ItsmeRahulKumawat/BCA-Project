# settings.py

class Settings():
    """A class to store all the settings of the game"""

    def __init__(self):
        """Initializes the game settings"""
        #screen settings
        self.screenwidth = 1300
        self.screenheight = 700
        self.bg_color = (200,230,230)
        self.trans = (0,0,1000,750)

        #rocket settings
        self.rocket_speed_factor = 2.5
        self.rocket_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 5
        self.bullet_width = 3
        self.bullet_height = 20
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5

        # alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # how quickly the game speeds up
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()
        # How quickly the alien point values increase
        self.score_scale = 2

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.rocket_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        # scoring
        self.alien_points = 1

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.rocket_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)






