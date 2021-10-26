import pygame
import os
from main_menu import WIDTH,HEIGHT,BUTTONS_WIDTH,BUTTONS_HEIGHT

"""need background texture and exit button texture"""
MENU_BUTTON_IMAGE1 = pygame.transform.scale(pygame.image.load(
    'Assets/backtomenu1.png').convert(), (BUTTONS_WIDTH, BUTTONS_HEIGHT))
MENU_BUTTON_IMAGE2 = pygame.transform.scale(pygame.image.load(
    'Assets/backtomenu2.png').convert(), (BUTTONS_WIDTH, BUTTONS_HEIGHT))
MENU_BUTTON = MENU_BUTTON_IMAGE1.get_rect().move(WIDTH*5//16,HEIGHT*12//16)

def highscores():
    pygame.font.init()
    colors = {'RED': (255, 0, 0), 'BLUE': (0, 0, 255),
            'GREEN': (0, 255, 0), 'BLACK': (0, 0, 0),
            'YELLOW': (255, 255, 0), 'WHITE': (255, 255, 255)}
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('High Scores')
    HIGHSCORES_BACKGROUND = pygame.transform.scale(
        pygame.image.load(
            os.path.join(
                "Assets", "space.png")), (WIDTH, HEIGHT))
    screen.blit(HIGHSCORES_BACKGROUND,(0,0))

    with open('highscores.txt', 'r') as highscores:
        highscores_list = highscores.readlines()
    print(highscores_list)
    for score in highscores_list:
        highscores_list[highscores_list.index(score)] = score[:-1]
    highscores_list.sort(reverse=True)
    highscores_list = highscores_list[:10]


    myfont = pygame.font.SysFont('comicsans', 40)
    skip = 0
    for score in highscores_list:
        text_img = myfont.render(score, True, 'WHITE')
        screen.blit(text_img, (550, 100 + skip))
        skip += 40

    screen.blit(MENU_BUTTON_IMAGE1,MENU_BUTTON)

    pygame.display.update()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                if MENU_BUTTON.collidepoint(pos):
                    button_clicked(screen)
                    running = False
def button_clicked(screen):
    screen.blit(MENU_BUTTON_IMAGE2,MENU_BUTTON)
    pygame.display.update()
    pygame.time.delay(100)
if __name__=="__menu__":
    highscores()