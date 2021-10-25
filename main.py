"""Main module of the game that supports all other modules
#menu
    #start game
        #draw a window 
        #start generating obsticles'
        #end of the game
            #score
            #play again
            #go into main menu
    #highscores
        #display list of highscores
    #exit
"""
import pygame
import main_menu
import game
import end_menu
import highscores


def main():
    running = True
    #event loop
    while running:
        option=main_menu()
        if option == 'play':
            game()
            end_menu()
        elif option == 'highscores':
            highscores()
        else:
            quit_game()
    