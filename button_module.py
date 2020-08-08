
import pygame.font

class Button():
    def __init__(self,screen,msg):
        self.screen = screen
        self.screen_rect =  screen.get_rect()

        # set the dimensions and the properties of the button
        self.width,self.height = 400,100
        self.button_color = (0,0,82)
        self.text_color = (200,230,230)
        self.font = pygame.font.SysFont(None, 70)

        # build the buttonn's rect object and center it
        self.rect = pygame.Rect(0,0,self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped once only
        self.prep_msg(msg)

    def prep_msg(self,msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
