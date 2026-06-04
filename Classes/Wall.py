import pygame

class Wall():
    def __init__(self, size, thickness, elasticity = 1):
        self.size = size
        self.thickness = thickness
        self.elasticity = elasticity
    