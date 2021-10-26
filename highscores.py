import pygame
from pygame import font
from pygame.locals import *
"""need background texture and exit button texture"""

# Dict of colors, just to not define them with RGB every time, can
# be broadened.
colors = {'RED': (255, 0, 0), 'BLUE': (0, 0, 255),
          'GREEN': (0, 255, 0), 'BLACK': (0, 0, 0),
          'YELLOW': (255, 255, 0), 'WHITE': (255, 255, 255)}


def highscores_main():
    """A function that shows high scores list.
    """
    pygame.init()
    # setting screen, aming it and giving a bg-color
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('High Scores')
    screen.fill('BLACK')

    # creating a button
    button_menu = pygame.Surface((200, 100))
    button_menu = pygame.image.load('Assets/backtomenu1.png')
    button_menu = pygame.transform.scale(button_menu, (300, 100))
    screen.blit(button_menu, (500, 550))
    # Making a .Rect object from th e .Surface object
    button_menu = button_menu.get_rect()

    # reading highscores from a local file, sorting them and
    #  showing top-10 results
    with open('highscores.txt', 'r') as highscores:
        highscores_list = highscores.readlines()
    for score in highscores_list:
        highscores_list[highscores_list.index(score)] = score[:-1]
    highscores_list.sort(reverse=True)
    highscores_list = highscores_list[:10]

    # degining a font from the system fonts
    myfont = pygame.font.SysFont(None, 40)
    # A gap btw the first and every next row of scores
    skip = 0

    # a loop which writes scores on the screen
    for score in highscores_list:
        text_img = myfont.render(score, True, 'WHITE')
        screen.blit(text_img, (550, 100 + skip))
        skip += 40

    # updating screen and starting an event loop
    pygame.display.update()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            """Тут треба розібратись чого не паше клік"""
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if button_menu.collidepoint(pos):
                    button_menu = pygame.image.load('Assets/backtomenu2.png')
                    button_menu = pygame.transform.scale(button_menu, (300,
                                                                       100))
                    screen.blit(button_menu, (500, 550))
                    print('if you can see this then burron works')


if __name__ == '__main__':
    highscores_main()
