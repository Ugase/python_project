import pygame
from pygame.locals import *
import sys

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 720))
# position = [1280//2, 720//2]
position = [123, 321]
pygame.draw.circle(screen, pygame.Color(255, 255, 255), tuple(position), 10.0)
player = pygame.image.load("E:\Coding_Projects\Python\dl1\player.png")
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_w]:
        position[1] -= 1 * dt
    if pressed_keys[K_s]:
        position[1] += 1 * dt
    if pressed_keys[K_a]:
        position[0] -= 1 * dt
    if pressed_keys[K_d]:
        position[0] += 1 * dt
    if position == [123,321]:
    screen.blit(player, position)
    pygame.display.flip()
    screen.fill(pygame.Color(0, 0, 0))
    dt = 1