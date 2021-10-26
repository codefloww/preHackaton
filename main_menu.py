"""Module that shows a main menu screen, handles clickes and 
recognises which button is clicked"""
import pygame
import os
# Size of the screen of the game
WIDTH = 1280
HEIGHT = 720
# Sizes of buttons
BUTTONS_WIDTH = WIDTH*6//16
BUTTONS_HEIGHT = HEIGHT//9
# Sizes of title
TITLE_WIDTH = WIDTH*10//16
TITLE_HEIGHT = HEIGHT*4//16
# Background of the main menu
MAIN_BACKGROUND = pygame.transform.scale(
    pygame.image.load(
        os.path.join(
            "Assets", "menu_background.png")), (WIDTH, HEIGHT))
# initializing screen
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("NAME OF THE GAME")
# creating and adding to screen title
TITLE = pygame.transform.scale(pygame.image.load(
    os.path.join("Assets", "Witch1.png")), (TITLE_WIDTH, TITLE_HEIGHT))
TITLE_LABEL = TITLE.get_rect().move(WIDTH*3//16, HEIGHT//16)
# creating buttons with images
# button play
BUTTON_PLAY_IMAGE1 = pygame.transform.scale(pygame.image.load(
    'Assets/buttonstart1.png').convert(), (BUTTONS_WIDTH, BUTTONS_HEIGHT))
BUTTON_PLAY_IMAGE2 = pygame.transform.scale(pygame.image.load(
    'Assets/buttonstart2.png').convert(), (BUTTONS_WIDTH, BUTTONS_HEIGHT))
BUTTON_PLAY = BUTTON_PLAY_IMAGE1.get_rect().move(
    WIDTH*5//16, (HEIGHT * 10 // 16) - 50)
# button highscores
BUTTON_HIGHSCORES_IMAGE1 = pygame.transform.scale(pygame.image.load(
    'Assets/buttonscore1.png').convert(), (BUTTONS_WIDTH, BUTTONS_HEIGHT))
BUTTON_HIGHSCORES_IMAGE2 = pygame.transform.scale(pygame.image.load(
    'Assets/buttonscore2.png').convert(), (BUTTONS_WIDTH, BUTTONS_HEIGHT))
BUTTON_HIGHSCORES = BUTTON_HIGHSCORES_IMAGE1.get_rect().move(WIDTH*5 //
                                                             16, HEIGHT*11//16)
# button exit
BUTTON_EXIT_IMAGE1 = pygame.transform.scale(pygame.image.load(
    'Assets/buttonexit1.png').convert(), (BUTTONS_WIDTH, BUTTONS_HEIGHT))
BUTTON_EXIT_IMAGE2 = pygame.transform.scale(pygame.image.load(
    'Assets/buttonexit2.png').convert(), (BUTTONS_WIDTH, BUTTONS_HEIGHT))
BUTTON_EXIT = BUTTON_EXIT_IMAGE1.get_rect().move(
    WIDTH*5//16, (HEIGHT * 12 // 16) + 50)

# dictionaries of buttons and their images
BUTTONS = {"PLAY": BUTTON_PLAY,
           "HIGHSCORES": BUTTON_HIGHSCORES, "EXIT": BUTTON_EXIT}
IMAGES = {"PLAY": [BUTTON_PLAY_IMAGE1, BUTTON_PLAY_IMAGE2],
          "HIGHSCORES": [BUTTON_HIGHSCORES_IMAGE1, BUTTON_HIGHSCORES_IMAGE2],
          "EXIT": [BUTTON_EXIT_IMAGE1, BUTTON_EXIT_IMAGE2]}


def click_button(button: str):
    """Changes state of button

    Args:
        str: which button was clicked
    """
    WIN.blit(IMAGES[button][1], BUTTONS[button])
    pygame.display.update()
    pygame.time.delay(100)


def draw_win():
    """updates all instances of screen including itself
    """
    # drawing all the instances of the screen
    WIN.blit(MAIN_BACKGROUND, (0, 0))
    WIN.blit(TITLE, TITLE_LABEL)
    WIN.blit(IMAGES["PLAY"][0], BUTTONS["PLAY"])
    WIN.blit(IMAGES["HIGHSCORES"][0], BUTTONS["HIGHSCORES"])
    WIN.blit(IMAGES["EXIT"][0], BUTTONS["EXIT"])
    # update screen
    pygame.display.update()


def main_menu() -> str:
    """Maintains a main_menu screen and interaction with it

    Returns:
        str: A name of the button that was clicked
    """
    running = True
    clicked = ''
    # event loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # checks for the clicks on buttons
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if BUTTON_PLAY.collidepoint(pos):
                    clicked = "PLAY"
                elif BUTTON_HIGHSCORES.collidepoint(pos):
                    clicked = "HIGHSCORES"
                elif BUTTON_EXIT.collidepoint(pos):
                    clicked = "EXIT"
            if clicked != '':
                click_button(clicked)
                running = False


        draw_win()
    return clicked


if __name__ == "__main__":
    print(main_menu())
