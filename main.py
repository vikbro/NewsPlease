import pygame
from game.settings import *
from game.model.game import Game
import sys

# profiling
# import cProfile
# import pstats

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill((255, 255, 255))
    pygame.display.set_caption('News Please')
    clock = pygame.time.Clock()

    game = Game()
    game.run(clock)

pygame.quit()
sys.exit()
