import pygame

class popButton():
    pygame.font.init() 
    base_font = pygame.font.Font(None,32)
    text_surface= None
    def __init__(self,screen) -> None:
        self.screen = screen
        self.button =  pygame.Rect(400,500,200,60)

    def display(self):
        pygame.draw.rect(self.screen, (255,0,0),self.button)
        self.text_surface = self.base_font.render("POP",False,(0,0,255))
        self.screen.blit(self.text_surface, (self.button.x + 70,self.button.y + 20))
        
        