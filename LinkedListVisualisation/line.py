import pygame

class Line():
    def __init__(self,left_point,right_point) -> None:
        self.left_point = left_point
        self.right_point = right_point

    def display(self,screen):
        pygame.draw.line(screen,(40,100,40),self.left_point,self.right_point)
