import pygame
from paddle import Paddle
from colors import *
from ball import Ball
from blocks import BlockArray
# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 1200
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Break Out")


# Create an instance of RectangularSprite
paddle = Paddle(screen, 150, 30, WHITE)
PADDLE_SPEED = 5

ball = Ball(screen, 15, BLUE, (1200//2,855))
blocks = BlockArray(screen, 20)
blocks.initialize_block_pos()



# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ball.velocity[0]+=3
                ball.velocity[1]-=3
            if event.key == pygame.K_LEFT:
                paddle.speed = -PADDLE_SPEED  # Move left
            elif event.key == pygame.K_RIGHT:
                paddle.speed = PADDLE_SPEED  # Move right
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                 paddle.speed = 0 

    # Update sprite position
    paddle.update()
    PADDLE_SPEED*=1.0005
    ball.update(paddle)
    # Fill the screen with black (or any other background color)
    if ball.position[1] > screen_height:
        pygame.quit()

    screen.fill(BLACK)

    # Draw the sprite
    paddle.draw()
    ball.draw()
    blocks.draw_blocks()
    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
