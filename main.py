import pygame
from Classes.Ball import Balls
from Classes.constants import *

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True


ball_list = []

def create_ball(ball_id, pos, elas, col, rad):
    ball_id = Balls(pos, elas, col, rad)
    ball_list.append(ball_id)
    return ball_id

ball_1 = create_ball("ball_1", [100,200], 0.9, "blue", 25.0)
ball_2 = create_ball("ball_2", [200, 200], 0.8, "green", 40.0)


while running:
    screen.fill((0,0,0))
    mouse = list(pygame.mouse.get_pos())

    for ball in ball_list:
        ball.ob = ball.draw(screen)
        ball.gravity()
        ball.collides_barrier()
        ball.update()
        ball.collides_mouse(mouse)

    ball_1.check_collision(ball_2)
    ball_1.find_overlap(ball_2)
    ball_1.resolve_overlap(ball_2)
    ball_1.resolve_collision(ball_2)

    ball_2.check_collision(ball_1)
    ball_2.find_overlap(ball_1)
    ball_2.resolve_overlap(ball_1)
    ball_2.resolve_collision(ball_1)

    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for ball in ball_list:
                if ball.ob.collidepoint(mouse):
                    ball.clicked = True
        if event.type == pygame.MOUSEBUTTONUP:
            for ball in ball_list:
                if ball.ob.collidepoint(mouse):
                    ball.clicked = False
   
    pygame.display.flip()
    clock.tick(60)
pygame.quit()


