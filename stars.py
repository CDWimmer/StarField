import pygame
from collections import deque
import random

class stars(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        random.seed(3)
        self.stars = deque()
        self.updateStarfield()

    def draw(self, surface):
        for star in self.stars:
            pygame.draw.circle(surface, star[0], star[1], star[2], 0)
        
    def pickColour(self):
        colour = random.randrange(0,5)
        if colour == 0: # Red
            blueTint = random.randrange(50,128)
            return (random.randrange(200,255), blueTint, blueTint)
        if colour == 1: # Blue
            return (random.randrange(220, 255), random.randrange(220,255), random.randrange(220, 255))
        if colour == 2: # Orange
            orange = random.randrange(200,255)
            return (orange, orange, random.randrange(50, 128))    
        # White
        lightTint = random.randrange(200,255) 
        return (200, lightTint, lightTint)


    def updateStarfield(self):
        tempDeque = deque()
        for i in range(0, 40):
            tempDeque.append((self.pickColour(), (random.randrange(0,self.width), random.randrange(0,self.height)), random.randrange(1,7,2)))
        
        self.stars = tempDeque
