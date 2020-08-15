#import modules
import pygame
#level of the game
def level():
    pass
# display game main menu
def renderMainMenu():
    pass
# start game
def renderGame():
    pass
def SpawnCharacter():
    pass
#initialize game
pygame.init()
#screen size
screenWidth=800
screenhieght=400
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pygame.display.set_mode((screenWidth, screenHeight))
pygame.quit
