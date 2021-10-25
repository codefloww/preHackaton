import pygame
from typing_extensions import runtime
"""we need a background and three buttons pixel assets
also there need to be two textures for the buttons(one for
hover and one for clicked"""
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill((255,255,255))
pygame.display.update()
running = True
#event loop
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
pygame.quit()