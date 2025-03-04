"""
TODO: DOCSTRING
"""
import pygame

from constants import *
from player import Player


def main():
    pygame.init()
    window = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    time = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(window, color=(0, 0, 0))
        player.draw(window)
        dt = time.tick(60) / 1000
        pygame.display.flip()


    # print("Starting Asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
