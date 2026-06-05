import pygame



class Balls():
    def __init__(self, pos = [50, 50], elasticity = 0.9, color = "red", radius = 25.0):
        self.pos = pygame.Vector2(pos[0], pos[1])
        self.elas = elasticity
        self.col = color
        self.rad = radius
        self.speed = pygame.Vector2([0,0])
        self.suspended = True
        self.bounce_count = 0
        


    def draw(self, surface):
        ball = pygame.draw.circle(surface, self.col, self.pos, self.rad)

    def gravity(self, grav = 0.5):
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
            self.pos[1 ] == 750 - self.rad
            self.suspended = False
        
    def move(self):
        self.gravity()
        self.bounce()

    #def check_input(self):
        #for event in pygame.event.get():
            #if event.type == pygame.MOUSEBUTTONDOWN:
                #mouse_pos = pygame.mouse.get_pos()
                #self.pos = mouse_pos
                

    def update(self):
        self.move()

    
        
