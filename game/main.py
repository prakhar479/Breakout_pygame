import pygame
from paddle import Paddle
from constants import *
from ball import Ball
from blocks import BlockArray


"""
PADDLE SIDE COLLISION LEFT 
"""



# Initialize Pygame
pygame.init()

# Screen dimensions

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Break Out")


paddle = Paddle(screen, PADDLE_WIDTH, PADDLE_HEIGHT, WHITE)

ball = Ball(screen, BALL_RADIUS, BLUE, (SCREEN_WIDTH//2,SCREEN_HEIGHT - PADDLE_HEIGHT - BALL_RADIUS))
blocks = BlockArray(screen, BLOCK_COLUMNS, BLOCK_ROWS)
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
                ball.velocity[0]+=BALL_VELOCITY
                ball.velocity[1]-=BALL_VELOCITY
            if event.key == pygame.K_LEFT:
                paddle.speed = -PADDLE_SPEED  # Move left
            elif event.key == pygame.K_RIGHT:
                paddle.speed = PADDLE_SPEED  # Move right
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                 paddle.speed = 0 

    paddle.update()
    PADDLE_SPEED*=FRAME_MULT

    ball.update(paddle,blocks)

    if ball.position[1] > SCREEN_HEIGHT:
        running = False

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
