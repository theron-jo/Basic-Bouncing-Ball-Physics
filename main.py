import pygame
from Classes.Ball import Balls

pygame.init()
screen = pygame.display.set_mode((1280, 750))
clock = pygame.time.Clock()
running = True
object_list = []

Ball_1 = Balls()
object_list.append(Ball_1)


while running:
    screen.fill("black")
    mouse_pos = pygame.mouse.get_pos()

    Ball_1.draw(screen)
    Ball_1.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for object in object_list:
                if object.surface.collidepoint(mouse_pos):
                    object.pos[1] = mouse_pos[1] 
                    object.pos[0] = mouse_pos[0]
                    object.speed = [0,0]


    

    
    

    pygame.display.flip()
    clock.tick(60)
pygame.quit()


