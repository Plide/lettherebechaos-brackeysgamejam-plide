import pygame
import math

# Defining important variables
pygame.init()
keys = pygame.key.get_pressed()
clock = pygame.time.Clock()

# LEVEL DESIGN
rects = []
rects.append(pygame.Rect(0, 200, 200, 50))
rects.append(pygame.Rect(0, 282, 300, 50))
rects.append(pygame.Rect(400, 310, 80, 50))

# Screen stuff
bg_color = 204, 255, 220
screen_y = 360
screen_x = 480
screen = pygame.display.set_mode((screen_x, screen_y))

# Player's img and start coordinates.
player_img = pygame.image.load("player.png").convert()
player_y = 0
player_x = 0
player_y_velocity = 0
player_x_velocity = 0
coyote = 0


def pic(img, x, y):
    screen.blit(img, (x + 0, y + 0))


def main():
    screen.fill(bg_color)
# Get the variables global
    global player_y             # Y position of player
    global player_x             # X position of player
    global player_y_velocity    # Y velocity of player
    global player_x_velocity    # X velocity of player
    global coyote               # Checks if you are on ground, and gives a bit of extra frames to jump if not.
    global rects

# Inputs
    if pygame.key.get_pressed()[pygame.K_UP] and coyote > 0:
        player_y_velocity = -9
        coyote = 0

# This makes your jump lower when you release!
    if not pygame.key.get_pressed()[pygame.K_UP] and player_y_velocity < -1:
        player_y_velocity = -1

# Move left/right when pressing left/right!
    player_x_velocity = (pygame.key.get_pressed()[pygame.K_RIGHT] - pygame.key.get_pressed()[pygame.K_LEFT]) * 2.5

# Velocity effects
    player_y_velocity += 0.4
    player_y_velocity = min(player_y_velocity, 10)
    player_x += player_x_velocity
    player_y += player_y_velocity
    coyote -= 1
# Rectangles
    player_rect = pygame.Rect(player_x, player_y, 32, 32)

    # !!Collision!!
    for rect in rects:
        for i in range(10):
            if player_rect.colliderect(rect):
                player_y -= 1
                player_y_velocity = 0.5
                coyote = 4
                player_rect = pygame.Rect(player_x, player_y, 32, 32)
            else:
                break
    # Draw stuff (pic is a function I made to shorten the blit)
    pic(player_img, player_x, player_y)
    for rect in rects:
        pygame.draw.rect(screen, (64, 0, 0), rect)


# Main script
while True:
    main()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    if player_y > 376:
        pygame.quit()
        break
    clock.tick(60)
