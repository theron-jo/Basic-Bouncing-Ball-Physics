import pygame
from Classes.Ball import Balls
from Classes.constants import *

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

Ball_1 = Balls()
Ball_2 = Balls([150,150])
object_list = [Ball_1, Ball_2]



while running:
    screen.fill("black")
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())


    for object in object_list:
        object.draw(screen)
        object.update(mouse_pos)
        object.collides_ball(object_list)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for object in object_list:
                object.select_check(event.pos)
        if event.type == pygame.MOUSEBUTTONUP:
            for object in object_list:
                object.clicked = False



    

    
    

    pygame.display.flip()
    clock.tick(60)
pygame.quit()


