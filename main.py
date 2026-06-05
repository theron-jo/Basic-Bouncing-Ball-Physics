import pygame
from Classes.Ball import Balls

pygame.init()
screen = pygame.display.set_mode((1280, 750))
clock = pygame.time.Clock()
running = True

Ball_1 = Balls()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            Ball_1.pos[1] = mouse_pos[1] 
            Ball_1.pos[0] = mouse_pos[0]
            Ball_1.speed = [0,0]


    screen.fill("black")
    Ball_1.draw(screen)
    Ball_1.update()

    
    

    pygame.display.flip()
    clock.tick(60)
pygame.quit()


