
import pygame


# ── Window configuration ────────────────────────────────
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# ── Grid configuration ──────────────────────────────────
ROWS = 5
COLS = 5
GRID_SIZE = 100  # Width and height of one cell in pixels

# ── Player configuration ────────────────────────────────
PLAYER_SIZE = GRID_SIZE // 2
PLAYER_COLOR = (255, 68, 154)
GRID_COLOR = (0, 0, 0)
BACKGROUND_COLOR = (255, 255, 255)
GOAL_COLOR = (0, 180, 0)

# The player's logical starting position: (row, column)
START_ROW = 0
START_COL = 0

# The goal occupies the bottom-right cell
GOAL_ROW = ROWS - 1
GOAL_COL = COLS - 1


def get_cell_rect(row, col, x_offset, y_offset):
    """Return the pixel rectangle for a particular grid cell."""
    x = x_offset + col * GRID_SIZE
    y = y_offset + row * GRID_SIZE

    return pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)


def get_player_rect(row, col, x_offset, y_offset):
    """Convert the player's grid position into a centered pixel rectangle."""
    cell = get_cell_rect(row, col, x_offset, y_offset)

    # Center the smaller player rectangle inside its current cell.
    x = cell.x + (GRID_SIZE - PLAYER_SIZE) // 2
    y = cell.y + (GRID_SIZE - PLAYER_SIZE) // 2

    return pygame.Rect(x, y, PLAYER_SIZE, PLAYER_SIZE)


def draw_grid(screen, x_offset, y_offset):
    """Draw the grid by visiting every row and column."""
    for row in range(ROWS):
        for col in range(COLS):
            cell = get_cell_rect(row, col, x_offset, y_offset)
            pygame.draw.rect(screen, GRID_COLOR, cell, 1)


def environment():
    """Initialize and run the manually controlled Grid World."""

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("ECHO - Grid World")
    clock = pygame.time.Clock()

    # Center the entire grid inside the window.
    grid_width = COLS * GRID_SIZE
    grid_height = ROWS * GRID_SIZE

    x_offset = (SCREEN_WIDTH - grid_width) // 2
    y_offset = (SCREEN_HEIGHT - grid_height) // 2

    # Track the player using grid coordinates, not pixel coordinates.
    player_row = START_ROW
    player_col = START_COL

    # Prevent a held key from moving the player every single frame.
    movement_ready = True

    running = True

    while running:

        # ── Handle window events ─────────────────────────
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # ── Read keyboard state ──────────────────────────
        keys = pygame.key.get_pressed()

        # Check whether any movement key is currently held.
        movement_keys_held = (
            keys[pygame.K_UP]
            or keys[pygame.K_DOWN]
            or keys[pygame.K_LEFT]
            or keys[pygame.K_RIGHT]
        )

        # Allow another move only after all arrow keys are released.
        if not movement_keys_held:
            movement_ready = True

        # ── Calculate the next grid position ─────────────
        if movement_ready:
            next_row = player_row
            next_col = player_col

            if keys[pygame.K_UP]:
                next_row -= 1
            elif keys[pygame.K_DOWN]:
                next_row += 1
            elif keys[pygame.K_LEFT]:
                next_col -= 1
            elif keys[pygame.K_RIGHT]:
                next_col += 1
            else:
                # No movement key is pressed.
                next_row = player_row
                next_col = player_col

            # Only accept positions inside the grid boundaries.
            if 0 <= next_row < ROWS and 0 <= next_col < COLS:
                player_row = next_row
                player_col = next_col

            # Require a key release before the next movement.
            if movement_keys_held:
                movement_ready = False

        # ── Draw the current frame ───────────────────────
        screen.fill(BACKGROUND_COLOR)

        draw_grid(screen, x_offset, y_offset)

        # Draw the goal in the bottom-right cell.
        goal_rect = get_cell_rect(
            GOAL_ROW, GOAL_COL, x_offset, y_offset
        )
        pygame.draw.rect(screen, GOAL_COLOR, goal_rect)

        # Draw the player using its current logical position.
        player_rect = get_player_rect(
            player_row, player_col, x_offset, y_offset
        )
        pygame.draw.rect(screen, PLAYER_COLOR, player_rect)

        pygame.display.flip()
        clock.tick(FPS)

    # Release Pygame resources after the window closes.
    pygame.quit()


if __name__ == "__main__":
    environment()
