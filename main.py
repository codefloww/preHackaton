"""Main module of the game that supports all other modules
"""
import main_menu
import game
import end_menu
import highscores
import pygame


def main():
    """Maintains a whole process of application
    """
    pygame.init()
    running = True
    # event loop
    while running:
        # returns which button player have clicked

        option_menu = main_menu.main_menu()
        if option_menu == 'PLAY':
            option_end = 'AGAIN'
            while option_end == "AGAIN":
                game.game()
                option_end = end_menu.end_menu()
            if option_end == "HIGHSCORES":
                highscores.highscores()
        elif option_menu == 'HIGHSCORES':
            highscores.highscores()
        else:
            running = False
    pygame.quit()


if __name__ == "__main__":
    main()
