import pygame
import os
from pygame.locals import *
from highscores import get_highscores, write_highscore
from main_menu import WIDTH, HEIGHT
import random
"""Need texture for background, texture for witch and obsticles"""
pygame.font.init()
FPS = 60
SPELL_VEL = 5
BAT_VEL = 5
BAT_HIT = pygame.USEREVENT + 1
WITCH_HIT = pygame.USEREVENT + 2
TIMER = pygame.USEREVENT +3
GAME_BACKGROUND = pygame.transform.scale(pygame.image.load(
    'Assets/Background.png').convert(), (WIDTH, HEIGHT))
WITCH_SIZE = (WIDTH*2//16, HEIGHT*2//9)
WITCH_IMAGE = pygame.image.load(
    os.path.join("Assets", "Witch1.png"))
WITCH = pygame.transform.scale(
    WITCH_IMAGE, WITCH_SIZE)
BAT_SIZE = (160, 90)
BAT_IMAGE = pygame.image.load(
    os.path.join("Assets", "bat2.0.png"))
BAT = pygame.transform.rotate(pygame.transform.scale(
    BAT_IMAGE, BAT_SIZE), -90)
SPELL_SIZE = (90, 90)
SPELL_IMAGE = pygame.image.load(
    os.path.join("Assets", "fireball.png"))
SPELL = pygame.transform.scale(
    SPELL_IMAGE, SPELL_SIZE)
SCORE_FONT = pygame.font.SysFont("comicsans", 60)


def draw_win(WIN, witch, spells, bats, score,countdown):
    WIN.blit(GAME_BACKGROUND, (0, 0))
    your_score = SCORE_FONT.render(str(score), 1, (255, 255, 255))
    WIN.blit(your_score, (WIDTH//2, HEIGHT*8//9))
    WIN.blit(WITCH, (witch.x, witch.y))
    countdown = SCORE_FONT.render(str(countdown),1,(255,255,255))
    WIN.blit(countdown,(WIDTH*15//16,HEIGHT*8//9))
    if len(spells) != 0:
        WIN.blit(SPELL, (spells[0].x, spells[0].y))

    for bat in bats:
        WIN.blit(BAT, (bat.x, bat.y))
    pygame.display.update()
# def spam_bats():


def witch_movement_handle(key_pressed, witch):
    if key_pressed == pygame.K_UP and witch.y >= 30:
        witch.y -= 200
    if key_pressed == pygame.K_DOWN and witch.y < 400:
        witch.y += 200


def spell_handle(spells, bats):
    for spell in spells:
        if spell.x < WIDTH//2:
            spell.x += SPELL_VEL
        elif spell.x >= (WIDTH//2) - SPELL_SIZE[0]:
            spells.remove(spell)
    if len(spells)!=0:
        for bat in bats:
            if spells[0].colliderect(bat):
                pygame.event.post(pygame.event.Event(BAT_HIT))
                bats.remove(bat)
                spells.remove(spells[0])
                break
            elif spells[0].x > WIDTH:
                spells.remove(spells[0])


def bats_handle(bats, witch):
    for bat in bats:
        bat.x -= BAT_VEL
        if witch.colliderect(bat):
            pygame.event.post(pygame.event.Event(WITCH_HIT))
        elif bat.x < 0:
            bats.remove(bat)
            pygame.event.post(pygame.event.Event(BAT_HIT))


def spam_bats(bats):
    row = random.randint(0,2)
    bat=pygame.Rect(WIDTH*15//16,60+200*row,*BAT_SIZE)
    bats.append(bat)

def game():
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    witch = pygame.Rect(50, 200, *WITCH_SIZE)
    score = 0
    bats = []
    spells = []
    countdown = ""
    clock = pygame.time.Clock()
    counter, text = 100, '100'.rjust(3)
    pygame.time.set_timer(TIMER,1000)
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == WITCH_HIT:
                running = False
            if event.type == TIMER:
                spam_bats(bats)
                counter-=1
                if counter>0:
                    countdown = str(counter).rjust(3)
                else:
                    pygame.event.post(pygame.event.Event(QUIT))
                    countdown = 0
                    
            if event.type == BAT_HIT:
                score += 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and len(spells) == 0:
                    spell = pygame.Rect(
                        witch.x+WITCH_SIZE[0], witch.y+WITCH_SIZE[1]//2, *SPELL_SIZE)
                    spells.append(spell)
                if event.key == pygame.K_UP:
                    witch_movement_handle(pygame.K_UP, witch)
                if event.key == pygame.K_DOWN:
                    witch_movement_handle(pygame.K_DOWN, witch)

        if score > 100:
            running = False
        spell_handle(spells, bats)
        bats_handle(bats, witch)
        draw_win(WIN, witch, spells, bats, score,countdown)
    #implement living 3 minutes
    # implement saving a highscore
    highscores=get_highscores()
    if len(highscores)<10:
        highscores.append((str(score)))
    else:
        for i in range(len(highscores)):
            if int(highscores[i])<score:
                highscores.insert(i,(str(score)))
                break
    write_highscore(highscores)


if __name__ == "__main__":
    game()
