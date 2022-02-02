
# Imports
import pygame,sys, Player

# Constants
import World

WIDTH, HEIGHT = 1000, 1000
TITLE = "Motherload Python"

# Window initialization
pygame.init()
screen = pygame.display.set_mode((HEIGHT,WIDTH))
pygame.display.set_caption(TITLE)

# Game initialization
clock = pygame.time.Clock()
running = True
world = World.World(15, 15)
player = Player.Player(350, 250)

# -------- Main Program Loop -----------
while running:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            running = False  # Flag that we are done so we can exit the while loop
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.left_pressed = True
            if event.key == pygame.K_RIGHT:
                player.right_pressed = True
            if event.key == pygame.K_UP:
                player.up_pressed = True
            if event.key == pygame.K_DOWN:
                player.down_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.left_pressed = False
            if event.key == pygame.K_RIGHT:
                player.right_pressed = False
            if event.key == pygame.K_UP:
                player.up_pressed = False
            if event.key == pygame.K_DOWN:
                player.down_pressed = False

    # --- Game logic

    print(player.x)
    if player.x < 0:
        player.x = 0
    if player.x + player.rect.width > WIDTH:
        player.x = WIDTH - player.rect.width
    if player.y < 0:
        player.y = 0


    # --- Drawing code
    screen.fill((12, 24, 36))

    world.draw(screen)
    player.draw(screen)

    # update
    player.update()
    pygame.display.flip()

    # --- Limit to 144 frames per second
    clock.tick(144)

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
