import pygame
from Point import *
from line import *
class Node(pygame.sprite.Sprite):
    
    offset_x=0
    offset_y=0
    left_point_offset_x=0
    left_point_offset_y=0
    right_point_offset_x=0
    right_point_offset_y=0
    nodeactivecolor = (100,100,100)
    nodestandardcolor =255
    nodecolor = 255
    next_node = None
    line = None
    
    text_surface=None
    def __init__(self,head,x,y,width,height,screen) -> None:
        
        super().__init__()
        
        self.screen = screen
        self.value = ""
        self.x=x
        self.y=y
        self.base_font = pygame.font.Font(None,32)
        self.width=width
        self.height = height
        self.shape = pygame.Rect(x,y,self.width,self.height)
        self.is_head = head
        self.left_side_point = Point(self.x,self.y + self.height/2,5,self.screen)
        self.right_side_point =Point(self.x + self.width,self.y + self.height/2,5,self.screen)
        self.righ_side_standardx = self.x + self.width
        

        
        self.node_draging = False
        self.active = False

    def add_line(self):
        self.line = Line(self.right_side_point,self.next_node.left_side_point)
    def display(self):
        if self.active:
            self.nodecolor = self.nodeactivecolor
        else:
            if self.is_head == True:
                self.nodecolor = (30,50,80)
            else:
                self.nodecolor = self.nodestandardcolor
        pygame.draw.rect(self.screen, self.nodecolor,self.shape)
        self.left_side_point.display()
        self.text_surface = self.base_font.render(self.value,True,(255,0,0))
        self.shape.w=max(self.width,self.text_surface.get_width()+10)
        if self.shape.w > self.right_side_point.x-self.shape.x:
            self.right_side_point.x = self.shape.w + self.shape.x
        elif self.shape.w < self.right_side_point.x-self.shape.x:
            self.right_side_point.x = self.righ_side_standardx
            
            
            


        self.right_side_point.display()
        
            
        if self.next_node != None:
            coordsr = (self.right_side_point.x,self.right_side_point.y)
            coordsl = (self.next_node.left_side_point.x,self.next_node.left_side_point.y)
            self.line = Line(coordsr,coordsl)
            self.line.display(self.screen)
        
        self.screen.blit(self.text_surface, (self.shape.x+10, self.shape.y+10)) 

        
        
    
    def set_value(self,value):
        self.value = value

    def update(self,event_list,one_active,nodes):
        
        for event in event_list: 
            
                    
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                g=False
                            
                           
                if event.button ==1:
                    if self.shape.collidepoint(event.pos):
                        for node in nodes:
                            if pygame.Rect.colliderect(self.shape,node.shape) == True:
                                if node != self.shape:
                                    node.active = False
                                    node.node_draging = False

                        
                        self.node_draging = True    
                        self.active = True
                        mouse_x,mouse_y =event.pos
                        self.offset_x = self.shape.x - mouse_x
                        self.offset_y = self.shape.y - mouse_y
                        self.left_point_offset_x = self.left_side_point.x - mouse_x
                        self.left_point_offset_y = self.left_side_point.y - mouse_y
                        self.right_point_offset_x = self.right_side_point.x - mouse_x
                        self.right_point_offset_y = self.right_side_point.y - mouse_y
                        
                    else:
                        
                        self.active = False
                       
                        
                        
                        
                    
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button ==1:
                    self.node_draging=False
                    
            elif event.type == pygame.MOUSEMOTION:
                if self.node_draging:
                    mouse_x,mouse_y =event.pos 
                    self.shape.x = mouse_x + self.offset_x
                    self.shape.y = mouse_y + self.offset_y
                    self.left_side_point.x =mouse_x + self.left_point_offset_x
                    self.left_side_point.y =mouse_y + self.left_point_offset_y
                    self.right_side_point.x =mouse_x + self.right_point_offset_x
                    self.right_side_point.y = mouse_y+ self.right_point_offset_y
            if event.type == pygame.KEYDOWN and self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.value = self.value[:-1]
                else:
                    self.value += event.unicode
        
            
            
        
        
        
        
          
        