import pygame
pygame.init()

# Define some colors
WHITE = ( 255, 255, 255)

# Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Motherload Python")

# The loop will run until the user exits the game
running = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while running:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            running = False  # Flag that we are done so we can exit the while loop

        # --- Game logic

        # --- Drawing code

        # First, clear the screen to white.
    screen.fill(WHITE)
    # Then you can draw different shapes and lines or add text to your background stage.

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
