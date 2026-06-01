import pygame

class Balls():
    def __init__(self, pos = [0,0], color = "red", radius = 25.0, elasticity = 1):
        self.pos = pos
        self.color = color
        self.radius = radius
        self.movement = []
        self.elasticity = elasticity


    def Draw(self, surface):
        ball = pygame.draw.circle(surface, self.color, self.pos, self.radius)
        return ball
