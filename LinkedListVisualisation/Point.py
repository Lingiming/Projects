import pygame
class Point:
    def __init__(self,x,y,size,screen) -> None:
        self.screen = screen
        self.x = x
        self.y = y
        self.size = size
        self.colour = (0,255,0)
        self.thickness = 5
    def display(self):
        pygame.draw.circle(self.screen, self.colour, (self.x, self.y), self.size)