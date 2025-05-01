# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint

pygame.init()
res = (640, 480)
window = pygame.display.set_mode(res)
robot = pygame.image.load("robot.png")
rock = pygame.image.load("rock.png")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Sans Serif", 24)

robot_w, robot_h = robot.get_width(), robot.get_height()
robot_v = 4
wall = res[0] - robot_w
robot_x, robot_y = wall // 2, res[1] - robot_h

rock_w, rock_h = rock.get_width(), rock.get_height()
rock_v = 1
gnd = res[1] - rock_h
army, id = {}, 1
army_size, spawn = 3, 150

ctrl = {pygame.K_LEFT: False, pygame.K_RIGHT: False}
score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key in ctrl:
            ctrl[event.key] = True
        
        if event.type == pygame.KEYUP and event.key in ctrl:
            ctrl[event.key] = False

        if event.type == pygame.QUIT:
            exit()

    clock.tick(60)
    window.fill((0, 0, 40))

    # show score
    text = font.render(f"score: {score:3}", True, "white")
    window.blit(text, (550, 10))

    # control robot
    if ctrl[pygame.K_RIGHT] and robot_x < wall:
        robot_x += robot_v
    if ctrl[pygame.K_LEFT] and robot_x > 0:
        robot_x -= robot_v
    
    window.blit(robot, (robot_x, robot_y))

    # move asteroids
    if len(army) < army_size and randint(1, spawn) == 1:
        army[id] = [randint(0, 640 - rock_w), -rock_h]
        id = (id + 1) % 100
    
    dump = []
    for ast in list(army.keys()):
        x, y = army[ast]
        if y >= gnd:
            exit()
        elif y + rock_h >= robot_y and (
            robot_x <= x <= robot_x + robot_w or \
            robot_x <= x + rock_w <= robot_x + robot_w):
            score += 1
            if score and not score % 10:
                army_size += 1
            if score and not score % 20:
                if spawn > 10:
                    spawn -= 10
                robot_v += 1
            
            dump.append(ast)
        else:
            army[ast] = [x, y + rock_v]
        
        window.blit(rock, army[ast])

    for ast in dump:
        del army[ast]

    pygame.display.flip()
