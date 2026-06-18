import pygame, math
from Classes.constants import *
from Classes.Vector import *




class Balls():
    def __init__(self, pos = [50, 50], elasticity = 0.9, color = "red", radius = 25):
        self.pos = pos
        self.vel = [0,0]
        self.move = [False, False]
        self.elas = elasticity
        self.col = color
        self.rad = radius
        self.suspend = False
        self.clicked = False
        self.collide = False
        self.bounce_count = 0

    def draw(self, screen):
        circle = pygame.draw.circle(screen, self.col, (self.pos[0], self.pos[1]), self.rad)
        return circle

    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        

    def check_suspend(self):
        if (self.pos[1] + self.rad) < screen_height:
            self.suspend = True
        else:
            self.suspend = False

    def gravity(self):
        self.check_suspend()
        if not self.clicked and self.suspend:
            self.vel[1] += gravity

    def collides_barrier(self):
        #collision with left and right walls
        if self.pos[0] <= 0 + 2*self.rad:
            self.vel[0] = -self.vel[0] * self.elas
        if self.pos[0] >= screen_width - 2*self.rad:
            self.vel[0] = -self.vel[0] * self.elas

        #collision with floor. addtional code to ensure complete stop
        if self.pos[1] >= (screen_height - self.rad) and self.vel[1] > 0:
            self.vel[1] = -self.vel[1] * self.elas
        if self.pos[1] >= (screen_height - self.rad) and abs(self.vel[1]) <= 1:
            self.vel[1] == 0
            self.pos[1] == screen_height - self.rad
            self.suspended = False

    def collides_mouse(self, mouse_pos):
        if self.clicked == True:
            self.pos[0] = mouse_pos[0]
            self.pos[1] = mouse_pos[1]

    def check_collision(self, other):
        distance = get_distance(self.pos, other.pos)
        if (self.rad + other.rad) >= distance:
            self.collide = True
        else:
            self.collide = False

    def find_overlap(self, other):
        if self.collide == True:
            overlap = (self.rad + other.rad) - (get_distance(self.pos, other.pos))
            return overlap
        
    def resolve_overlap(self, other):
        if self.collide == True:
            overlap = self.find_overlap(other)
            self_mag = get_mag(self.pos)
            other_mag = get_mag(other.pos)
            self_mag -= overlap/2
            other_mag += overlap/2
            self.pos = normalize(self.pos)
            other.pos = normalize(other.pos)
            self.pos[0] = self.pos[0] * self_mag
            self.pos[1] = self.pos[1] * self_mag
            other.pos[0] = other.pos[0] * other_mag
            other.pos[1] = other.pos[1] * other_mag

    def resolve_collision(self, other):
        self.check_collision(other)
        self.resolve_overlap(other)
        if self.collide == True:
            self.vel[0] = -self.vel[0]
            self.vel[1] = -self.vel[1]
            relative_speed = get_relative_vector(self.vel, other.vel)
            self_reflect_angle = get_reflect_angle(self, other)


    

   

    
        
