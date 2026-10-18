
import pygame


# Window configuration
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Grid configuration
GRID_SIZE = 100  # Width and height of each square in pixels
ROWS = 5
COLS = 5

def user_block() -> pygame.Rect:
    """Return a rectangle representing the user-controlled block."""
    return pygame.Rect(0, 0, GRID_SIZE, GRID_SIZE)

def draw_grid(screen, x_offset, y_offset):
    """Draw the grid, centered within the window."""

    # Visit every cell using its row and column indices
    for row in range(ROWS):
        for col in range(COLS):

            # Convert the cell's grid coordinates into screen coordinates
            x = x_offset + col * GRID_SIZE
            y = y_offset + row * GRID_SIZE

            # Create a rectangle representing the current cell
            cell = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)

            # Draw only the border, leaving the cell interior transparent
            pygame.draw.rect(screen, (0, 0, 0), cell, 1)


def environment():
    """Initialize and run the Grid World environment."""

    # Initialize Pygame modules and create the game window
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("ECHO - Grid World")
    clock = pygame.time.Clock()

    # Calculate offsets so the grid stays centered in the window
    grid_width = COLS * GRID_SIZE
    grid_height = ROWS * GRID_SIZE

    x_offset = (SCREEN_WIDTH - grid_width) // 2
    y_offset = (SCREEN_HEIGHT - grid_height) // 2

    # Main loop: continue running until the window is closed
    running = True

    while running:

        # Process events such as closing the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the previous frame before drawing the next one
        screen.fill((255, 255, 255))

        # Render the current environment
        draw_grid(screen, x_offset, y_offset)

        # Display the completed frame and maintain the target frame rate
        pygame.display.flip()
        clock.tick(FPS)

    # Release Pygame resources after exiting the main loop
    pygame.quit()


if __name__ == "__main__":
    environment()
