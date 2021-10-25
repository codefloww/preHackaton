import pygame
import os
from typing_extensions import runtime
"""we need a background and three buttons pixel assets
also there need to be two textures for the buttons(one for
hover and one for clicked"""
WIDTH = 1280
HEIGHT = 720
BLACK = (10, 0, 0)
MAIN_BACKGROUND = pygame.transform.scale(
    pygame.image.load(
        os.path.join(
            "Assets", "space.png")), (WIDTH, HEIGHT))
BUTTONS_WIDTH = WIDTH*6//16
BUTTONS_HEIGHT = HEIGHT//9
TITLE_WIDTH = WIDTH*10//16
TITLE_HEIGHT = HEIGHT*4//16
TITLE = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "space.png")), (TITLE_WIDTH, TITLE_HEIGHT))
TITLE_LABEL = pygame.Rect(WIDTH*3//16,HEIGHT//16,TITLE_WIDTH,TITLE_HEIGHT)

BUTTON_PLAY = pygame.Rect(WIDTH*5//16, (HEIGHT * 10 //
                          16) - 50, BUTTONS_WIDTH, BUTTONS_HEIGHT)
BUTTON_HIGHSCORES = pygame.Rect(
    WIDTH*5//16, HEIGHT*11//16, BUTTONS_WIDTH, BUTTONS_HEIGHT)
BUTTON_EXIT = pygame.Rect(WIDTH*5//16, (HEIGHT * 12 //
                          16) + 50, BUTTONS_WIDTH, BUTTONS_HEIGHT)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("YOOOO")
PLAY = pygame.USEREVENT + 1
HIGHSCORES = pygame.USEREVENT + 2
EXIT = pygame.USEREVENT + 3


def draw_win():
    WIN.blit(MAIN_BACKGROUND,(0,0))
    pygame.draw.rect(WIN,BLACK,TITLE_LABEL)
    pygame.draw.rect(WIN, BLACK, BUTTON_PLAY)
    pygame.draw.rect(WIN, BLACK, BUTTON_HIGHSCORES)
    pygame.draw.rect(WIN, BLACK, BUTTON_EXIT)

    pygame.display.update()


def main_menu():
    running = True
    # event loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                if BUTTON_PLAY.collidepoint(pos):
                    return "PLAY"
                elif BUTTON_HIGHSCORES.collidepoint(pos):
                    return("HIGHSCORES")
                elif BUTTON_EXIT.collidepoint(pos):
                    return("EXIT")
           
        draw_win()
    pygame.quit()


print(main_menu())
