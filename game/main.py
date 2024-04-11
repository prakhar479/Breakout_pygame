import pygame
from paddle import Paddle
from constants import *
from ball import Ball
from blocks import BlockArray

"""
PADDLE SIDE COLLISION LEFT 
"""

global running
running = True
clock = pygame.time.Clock()



# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Break Out")
paddle = Paddle(screen, PADDLE_WIDTH, PADDLE_HEIGHT, WHITE)
ball = Ball(screen, BALL_RADIUS, BLUE, (SCREEN_WIDTH//2,SCREEN_HEIGHT - PADDLE_HEIGHT - BALL_RADIUS))
blocks = BlockArray(screen, BLOCK_COLUMNS, BLOCK_ROWS)
blocks.initialize_block_pos()


pygame.mixer.music.load(MUSIC_FILES[4])
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

def playGame():
    global running
    global PADDLE_SPEED

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle.speed = -PADDLE_SPEED  # Moves the paddle tp left
            elif event.key == pygame.K_RIGHT:
                paddle.speed = PADDLE_SPEED  # Move the paddle to right

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                 paddle.speed = 0 

    paddle.update()

    # Increasing the PADDLE_SPEED by .05% every frame
    PADDLE_SPEED*=FRAME_MULT

    ball.update(paddle,blocks)

    # Checks the death of ball into the infinite abyss
    if ball.position[1] > SCREEN_HEIGHT:
        # running = False
        global STATE
        STATE = "over"

    screen.fill(BLACK)

    # Draw the sprite
    paddle.draw()
    ball.draw()
    blocks.draw_blocks()
    # Update the display
    pygame.display.flip()


def StartGame():
    # Set background color
    screen.fill(BLACK)

    # Display a title or instructions
    font = pygame.font.Font(None, 36)  # Choose a font and size
    text_surface = font.render("Break Out! Press Space to Start", True, WHITE)
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text_surface, text_rect)

    # Update the display
    pygame.display.flip()

    # Wait for user input (space key press)
    for event in pygame.event.get():
        global STATE
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_SPACE:

                # Sets STATE to play to go to playGame
                STATE = "play"
                ball.velocity[0]+=BALL_VELOCITY
                ball.velocity[1]-=BALL_VELOCITY

        pygame.display.flip()


def gameOver():
    """
    This function displays the game over screen.
    """
    # Set background color
    screen.fill(BLACK)

    # Display a game over message
    font = pygame.font.Font(None, 36)  # Choose a font and size
    text_surface = font.render("Game Over! Press R to Restart", True, WHITE)
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text_surface, text_rect)

    # Update the display
    pygame.display.flip()

    # Wait for user input (R key press)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                resetGame()
# Exit the gameOver function
    # Update the display during wait
        pygame.display.flip()


def resetGame():
    ball.position = [SCREEN_WIDTH//2,SCREEN_HEIGHT - PADDLE_HEIGHT - BALL_RADIUS]
    paddle.rect = pygame.Rect(1100//2, 870, PADDLE_WIDTH, PADDLE_HEIGHT)
    # blocks.block_pos = []
    blocks.n = blocks.num_blocks * blocks.lines
    blocks.initialize_block_pos()
    global STATE
    STATE = "start"

    global BALL_VELOCITY
    BALL_VELOCITY = 3
    ball.velocity = [0,0]

    global PADDLE_SPEED
    PADDLE_SPEED = 5
    paddle.speed = 0


while running:
    match STATE:
        case "start":
            StartGame()

        case "play":
            playGame()

        case "over":
            gameOver()


    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
