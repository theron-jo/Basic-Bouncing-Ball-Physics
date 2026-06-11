import pygame
from Classes.constants import *
from math import atan2



class Balls():
    def __init__(self, pos = [50, 50], elasticity = 0.9, color = "red", radius = 25):
        self.rad = radius
        #position of object
        self.pos = pygame.Vector2(pos[0], pos[1])
        #position of the surface underlying the visible object
        self.coll_pos = pygame.Vector2([self.pos[0]-self.rad, self.pos[1]-self.rad])
        #instantiate a surface. a square of size 2r that moves with visible object
        self.surface = pygame.Rect(self.coll_pos[0], self.coll_pos[1], self.rad * 2, self.rad * 2)
        #all speeds and positions are vector objects to permit updates to the variables
        self.speed = pygame.Vector2([0,0])
        #elaticity will reduce speed on bounce
        self.elas = elasticity
        self.col = color
        #suspension will initiate gravity
        self.suspended = True
        #clicking will initiate user interaction
        self.clicked = False
        self.bounce_count = 0
        

    def gravity(self):
        if not self.clicked:
            if self.pos[1] <= screen_height-self.rad-10 and self.suspended == False:
                self.suspended = True
            if self.suspended:
                self.speed[1] += gravity
                self.pos[1] += self.speed[1]

    def collides_barrier(self):
        #collision with left and right walls
        if self.pos[0] <= 0 + self.rad:
            self.speed[0] = -self.speed[0] * self.elas
        if self.pos[0] >= screen_width - self.rad:
            self.speed[0] = -self.speed[0] * self.elas

        #collision with floor. addtional code to ensure complete stop
        if self.pos[1] >= (screen_height - self.rad) and self.speed[1] > 0:
            self.speed[1] = -self.speed[1] * self.elas
        if self.pos[1] >= (screen_height - self.rad) and abs(self.speed[1]) <= 1:
            self.speed[1] == 0
            self.pos[1] == screen_height - self.rad
            self.suspended = False

    def conservation_of_momentum(self, other):
        self_angle = self.pos.angle_to(other.pos)
        oth_angle = other.pos.angle_to(self.pos)
        tangent_2 = 2* (atan2(self.pos[0] - other.pos[0], self.pos[1] - other.pos[1]))
        
        self_new_angle = tangent_2 - self_angle
        self.pos.rotate(self_new_angle)
        oth_new_angle = tangent_2 - oth_angle
        other.pos.rotate(oth_new_angle)
        if self.speed[1] > self.speed[0]:
            
            self.speed[1] = -self.speed[1] * self.elas
            other.speed[1] += (self.speed [1] * (other.elas+self.elas)/other.elas)
            

    def collides_ball(self, object_list):
        for object in object_list:
            if object_list.index(self) != object_list.index(object):
                distance = self.pos.distance_to(object.pos)
                if distance <= 2*self.rad:
                    self.speed[0] = -self.speed[0]
                    self.conservation_of_momentum(object)
    
    def coll_update(self):
        self.surface[0] = self.pos[0] - self.rad
        self.surface[1] =  self.pos[1] - self.rad

    def select_check(self, mouse_pos):
        self.clicked = False
        if self.surface.collidepoint(mouse_pos):
            self.clicked = True
        return self.clicked
    
    def selected(self, mouse_pos):
        if self.clicked == True:
            self.pos = mouse_pos
            self.speed = [0, 0]

    def draw(self, surface):
        rect = pygame.draw.rect(surface, pygame.SRCALPHA, self.surface, self.rad*2)
        ball = pygame.draw.circle(surface, self.col, self.pos, self.rad)
        
    def move(self):
        self.gravity()
        self.collides_barrier()
    
               
    def update(self, mouse_pos):
        self.move()
        self.coll_update()
        self.selected(mouse_pos)

    
        
