import pygame
from Node import *
from Point import *
from append_button import *
from pop_button import *
from LList import *
from insert_button import *
from remove_button import *

pygame.init()
one_active =[False,]
FPS = 144
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
run=True
node_color = (255,255,255)
user_text=""
BUTTONAPPEND = appendButton(screen)
BUTTONPOP = popButton(screen)
BUTTONINSERT = insertButton(screen)
BUTTONREMOVE = removeButton(screen)
node = Node(True,30,30,60,60,screen)
linked_list = LList(screen)
linked_list.append(node)

nodes_list = [node]
nodes = pygame.sprite.Group([node])



clock = pygame.time.Clock()

while run :   
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button ==1:
                        if BUTTONAPPEND.button.collidepoint(event.pos):
                            new_node = Node(False,400,300,60,60,screen)
                            nodes_list.append(new_node)
                            linked_list.append(new_node)
                          
                            nodes = pygame.sprite.Group(nodes_list)
                           

                        if BUTTONPOP.button.collidepoint(event.pos):
                            linked_list.pop()
                            current_node = linked_list.head
                            nodes_list = []
                            while(current_node):
                                 nodes_list.append(current_node)
                                 current_node = current_node.next_node
                            
                            nodes = pygame.sprite.Group(nodes_list) 
                        
                        if BUTTONINSERT.button.collidepoint(event.pos):
                            current_node = None
                            for node in nodes_list:
                                if node.active == True:
                                    current_node = node
                            if current_node != None:
                                new_node = Node(False,400,300,60,60,screen)
                                nodes_list.append(new_node)
                                if current_node == linked_list.head:
                                    new_node.is_head=True
                                    new_node.next_node=linked_list.head
                                    linked_list.head.is_head=False
                                    linked_list.head=new_node
                                else:
                                    pointer=linked_list.head
                                    while(pointer.next_node!=current_node):
                                        pointer = pointer.next_node
                                    new_node.next_node=current_node
                                    pointer.next_node=new_node
                                    
                            nodes = pygame.sprite.Group(nodes_list) 
                        if BUTTONREMOVE.button.collidepoint(event.pos):
                            current_node = None
                            for node in nodes_list:
                                if node.active == True:
                                    current_node = node
                            if current_node != None:
                                if current_node == linked_list.head:
                                    linked_list.head = current_node.next_node
                                    current_node.is_head=False
                                    linked_list.head.is_head =True
                                    current_node.next_node=None
                                else:
                                    pointer = linked_list.head
                                    while(pointer.next_node != current_node):
                                        pointer = pointer.next_node
                                    if pointer.next_node.next_node == None:
                                        pointer.next_node=None
                                    else:
                                        pointer.next_node=current_node.next_node
                                


                                nodes_list = []
                                current_node = linked_list.head
                                while(current_node):
                                    nodes_list.append(current_node)
                                    current_node = current_node.next_node   
                                nodes = pygame.sprite.Group(nodes_list) 

                                                   
    
    
    for node in nodes:
         node.update(event_list,one_active,nodes_list)
    screen.fill((255, 255, 255))
    
    for node in nodes:
        node.display()  
    BUTTONAPPEND.display()
    BUTTONPOP.display()
    BUTTONINSERT.display()
    BUTTONREMOVE.display()
    
    pygame.display.flip()
    clock.tick(FPS)
    

pygame.quit()