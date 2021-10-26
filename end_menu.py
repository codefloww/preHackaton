import pygame
import os
from main_menu import WIDTH,HEIGHT,BUTTONS_WIDTH,BUTTONS_HEIGHT
END_BACKGROUND = pygame.transform.scale(
    pygame.image.load(
        os.path.join(
            "Assets", "space.png")), (WIDTH, HEIGHT))
BUTTON_MENU_IMAGE1 = pygame.transform.scale(pygame.image.load(
    'Assets/backtomenu1.png').convert(), (BUTTONS_WIDTH, BUTTONS_HEIGHT))
BUTTON_MENU_IMAGE2 = pygame.transform.scale(pygame.image.load(
    'Assets/backtomenu2.png').convert(), (BUTTONS_WIDTH, BUTTONS_HEIGHT))
BUTTON_MENU = BUTTON_MENU_IMAGE1.get_rect().move(
    WIDTH*5//16, (HEIGHT * 11 // 16) - 50)

BUTTON_AGAIN_IMAGE1 = pygame.transform.scale(pygame.image.load(
    'Assets/playagain1.png').convert(), (BUTTONS_WIDTH, BUTTONS_HEIGHT))
BUTTON_AGAIN_IMAGE2 = pygame.transform.scale(pygame.image.load(
    'Assets/playagain2.png').convert(), (BUTTONS_WIDTH, BUTTONS_HEIGHT))
BUTTON_AGAIN = BUTTON_AGAIN_IMAGE1.get_rect().move(
    WIDTH*5//16, (HEIGHT * 9 // 16) - 50)
IMAGES={"AGAIN":[BUTTON_AGAIN_IMAGE1,BUTTON_AGAIN_IMAGE2],
        "MENU": [BUTTON_MENU_IMAGE1,BUTTON_MENU_IMAGE2]}
BUTTONS={"AGAIN":BUTTON_AGAIN,"MENU": BUTTON_MENU}

def click_button(WIN,button):
    WIN.blit(IMAGES[button][1], BUTTONS[button])
    pygame.display.update()
    pygame.time.delay(100)


def draw_win(WIN):
    WIN.blit(END_BACKGROUND,(0,0))
    WIN.blit(IMAGES["AGAIN"][0],BUTTONS["AGAIN"])
    WIN.blit(IMAGES["MENU"][0],BUTTONS["MENU"])
    pygame.display.update()


def end_menu():
    WIN = pygame.display.set_mode((WIDTH,HEIGHT))
    WIN.blit(END_BACKGROUND,(0,0))
    clicked = ''
    running=True
    # event loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if BUTTON_MENU.collidepoint(pos):
                    clicked = "MENU"
                elif BUTTON_AGAIN.collidepoint(pos):
                    clicked = "AGAIN"
            
            if clicked != '':
                click_button(WIN,clicked)
                running = False

        draw_win(WIN)
    return clicked


if __name__=="__main__":
    print(end_menu())