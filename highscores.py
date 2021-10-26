import pygame
import os
from main_menu import WIDTH, HEIGHT, BUTTONS_WIDTH, BUTTONS_HEIGHT

"""need background texture and exit button texture"""
COLORS = {'RED': (255, 0, 0), 'BLUE': (0, 0, 255),
          'GREEN': (0, 255, 0), 'BLACK': (0, 0, 0),
          'YELLOW': (255, 255, 0), 'WHITE': (255, 255, 255)}
MENU_BUTTON_IMAGE1 = pygame.transform.scale(pygame.image.load(
    'Assets/backtomenu1.png').convert(), (BUTTONS_WIDTH, BUTTONS_HEIGHT))
MENU_BUTTON_IMAGE2 = pygame.transform.scale(pygame.image.load(
    'Assets/backtomenu2.png').convert(), (BUTTONS_WIDTH, BUTTONS_HEIGHT))
MENU_BUTTON = MENU_BUTTON_IMAGE1.get_rect().move(WIDTH*5//16, HEIGHT*12//16)
HIGHSCORES_BACKGROUND = pygame.transform.scale(
    pygame.image.load(
        os.path.join(
            "Assets", "space.png")), (WIDTH, HEIGHT))
pygame.font.init()
#pygame.display.set_caption('High Scores')
HIGHSCORES_BACKGROUND = pygame.transform.scale(
    pygame.image.load(
        os.path.join(
            "Assets", "space.png")), (WIDTH, HEIGHT))


def button_clicked(WIN,button):
    WIN.blit(MENU_BUTTON_IMAGE2, MENU_BUTTON)
    pygame.display.update()
    pygame.time.delay(100)


def draw_win(WIN, highscores_list):
    WIN.blit(HIGHSCORES_BACKGROUND, (0, 0))
    WIN.blit(MENU_BUTTON_IMAGE1, MENU_BUTTON)
    skip = 0
    myfont = pygame.font.SysFont('comicsans', 40)
    for score in highscores_list:
        text_img = myfont.render(score, True, 'WHITE')
        WIN.blit(text_img, (550, 100 + skip))
        skip += 40
    pygame.display.update()


def highscores():
    
    with open('highscores.txt', 'r') as highscores:
        highscores_list = highscores.readlines()
    print(highscores_list)
    for score in highscores_list:
        highscores_list[highscores_list.index(score)] = score[:-1]
    highscores_list.sort(reverse=True)
    highscores_list = highscores_list[:10]

    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    WIN.blit(HIGHSCORES_BACKGROUND, (0, 0))
    running = True
    clicked = ''
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if MENU_BUTTON.collidepoint(pos):
                    clicked='MENU'
                    button_clicked(WIN,clicked)
                    running = False
        if clicked!='':
            button_clicked(WIN,clicked)
            running = False
        draw_win(WIN, highscores_list)

if __name__ == "__main__":
    highscores()
