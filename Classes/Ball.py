import pygame



class Balls():
    def __init__(self, pos = [50, 50], elasticity = 0.9, color = "red", radius = 25):
        self.pos = pygame.Vector2(pos[0], pos[1])
        self.rad = radius
        self.coll_pos = pygame.Vector2([self.pos[0]-self.rad, self.pos[1]-self.rad])
        self.elas = elasticity
        self.col = color
        self.speed = pygame.Vector2([0,0])
        self.suspended = True
        self.surface = pygame.Rect(self.coll_pos[0], self.coll_pos[1], self.rad * 2, self.rad * 2)
        self.clicked = False
        self.bounce_count = 0
        

    def gravity(self, grav = 0.5):
        if not self.clicked:
            if self.pos[1] <= 750-self.rad-10 and self.suspended == False:
                self.suspended = True
            if self.suspended:
                self.speed[1] += grav
                self.pos[1] += self.speed[1]

    def bounce(self):
        if self.pos[1] >= (750 - self.rad) and self.speed[1] > 0:
            self.speed[1] = -self.speed[1] * self.elas
        if self.pos[1] >= (750 - self.rad) and abs(self.speed[1]) <= 1:
            self.speed[1] == 0
            self.pos[1] == 750 - self.rad
            self.suspended = False
    
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
        self.bounce()
    
               
    def update(self, mouse_pos):
        self.move()
        self.coll_update()
        self.selected(mouse_pos)

    
        
