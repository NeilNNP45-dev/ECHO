"""Launch the ECHO application window."""

import pygame
from echo.environments.grid_world import environment

WINDOW_SIZE = (800, 600)
BACKGROUND_COLOR = (0, 0, 0)


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("ECHO")
    screen.fill(BACKGROUND_COLOR)
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        environment()  # Call the environment function to display the grid world        

    pygame.quit()


if __name__ == "__main__":
    main()
