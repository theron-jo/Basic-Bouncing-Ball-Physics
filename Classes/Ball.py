import pygame
from Classes.constants import *
from Classes.Vector import *


class Balls():
    def __init__(self, pos = [50, 50], elasticity = 0.9, color = "red", radius = 25):
        self.pos = pos
        self.vel = [0,0]
        self.elas = elasticity
        self.col = color
        self.rad = radius
        self.mass = (3.14*self.rad**2)/2
        self.suspend = False
        self.clicked = False
        self.collide = False

    def draw(self, screen):
        circle = pygame.draw.circle(screen, self.col, (self.pos[0], self.pos[1]), self.rad)
        return circle
        # Must return an object that can be clicked.

    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        # Other functions update velocity. Position is only updated here, and in the mouse-click function
        

    def check_suspend(self):
        if (self.pos[1] + self.rad) < screen_height:
            self.suspend = True
        else:
            self.suspend = False
            # Requires an update to include logic that supports resting on another ball as not being suspended

    def gravity(self):
        self.check_suspend()
        if not self.clicked and self.suspend:
            self.vel[1] += gravity

    def collides_barrier(self):
        #collision with left and right walls
        if self.pos[0] <= 0 + self.rad and self.vel[0] < 0:
            self.vel[0] = -self.vel[0] * self.elas
        if self.pos[0] >= screen_width - self.rad and self.vel[0] > 0:
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
            self.vel[0] = 0
            self.vel[1] = 0

    def check_collision(self, other):
        distance = get_distance(self.pos, other.pos)
        if (self.rad + other.rad) >= distance:
            self.collide = True
            return distance
        else:
            self.collide = False

    def find_overlap(self, other):
        overlap = (self.rad + other.rad) - (get_distance(self.pos, other.pos))
        return overlap
        
    def resolve_overlap(self, other):
        overlap = self.find_overlap(other)
        self_mag = get_mag(self.pos)
        other_mag = get_mag(other.pos)
        self_mag -= overlap/2
        other_mag += overlap/2
        self.pos = normalize(self.pos)
        other.pos = normalize(other.pos)
        self.pos = multiply(self.pos, self_mag)
        other.pos = multiply(other.pos, other_mag)


    def resolve_collision(self, object_list):
        for object in object_list:
            if object_list.index(self) != object_list.index(object):
                distance = self.check_collision(object)
                if self.collide == True and (self.rad + object.rad) >= distance:
                    try:
                        self.resolve_overlap(object)
                        col_normal = normalize(get_relative_vector(self.pos, object.pos))
                        relative_vel = get_relative_vector(self.vel, object.vel)
                        normal_vel = get_dot(relative_vel, col_normal)
                        if normal_vel > 0:
                            return
                        self_vel = multiply(add_to(self.vel, normal_vel/2), self.elas)
                        if self.pos[0] + self_vel[0] <= screen_height - self.rad:
                            self.vel = self_vel
                        object_vel = multiply(sub_from(object.vel, normal_vel/2), object.elas)
                        if object.pos[0] + object_vel[0] <= screen_height - object.rad:
                            object.vel = object_vel                 
                        self.collide = False
                    except:
                        raise Exception ("unknown error detected")

