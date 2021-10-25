import pygame
from pygame import font
from pygame.locals import *
"""need background texture and exit button texture"""

colors = {'RED': (255, 0, 0), 'BLUE': (0, 0, 255),
          'GREEN': (0, 255, 0), 'BLACK': (0, 0, 0),
          'YELLOW': (255, 255, 0), 'WHITE': (255, 255, 255)}
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('High Scores')
background = (0, 0, 0)
screen.fill(background)

with open('game/highscores.txt', 'r') as highscores:
    highscores_list = highscores.readlines()
for score in highscores_list:
    highscores_list[highscores_list.index(score)] = score[:-1]
highscores_list.sort(reverse=True)
highscores_list = highscores_list[:10]


myfont = pygame.font.SysFont(None, 40)
skip = 0
for score in highscores_list:
    text_img = myfont.render(score, True, 'WHITE')
    screen.blit(text_img, (550, 100 + skip))
    skip += 40

pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
