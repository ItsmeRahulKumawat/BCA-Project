class Game_Stats():
    """Tracks statistics for Alien Invasion."""
    def __init__(self, setting_obj):
        """Initialize statistics."""
        self.setting_obj = setting_obj
        self.reset_stats()
        # Start Alien Invasion in an active state.
        self.game_active = False
        # high score should never be reset
        self.high_score = 0


    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.rockets_left = self.setting_obj.rocket_limit
        self.score = 0
        self.level = 1


