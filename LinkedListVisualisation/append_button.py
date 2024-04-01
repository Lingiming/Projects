import pygame

class appendButton():
    pygame.font.init()     
    text_surface=None
    base_font = pygame.font.Font(None,32)
    def __init__(self,screen) -> None:
        self.screen = screen
        self.button =  pygame.Rect(100,500,200,60)

    def display(self):
        pygame.draw.rect(self.screen, (0,255,0),self.button)
        self.text_surface = self.base_font.render("APPEND",False,(0,0,255))
        self.screen.blit(self.text_surface, (self.button.x + 50,self.button.y + 20))