import pygame
from Node import *

class LList():
    size = 0
    head = None
    def __init__(self,screen) -> None:
        self.screen = screen
    def append(self, value):
        new_node = value
        if self.head == None:
            self.head = new_node
            self.size+=1
            return
        current_node = self.head
        while(current_node.next_node):
            current_node = current_node.next_node
        current_node.next_node = new_node
        current_node.add_line()
        self.size+=1
    
    def pop(self):
        current_node = self.head
        while(current_node.next_node.next_node):
            current_node = current_node.next_node
        current_node.next_node = None

    def print(self):
        current_node = self.head
        
        while(current_node.next_node):
            
            
            current_node = current_node.next_node
        