import pygame
from paddle import Paddle
from constants import *
from ball import Ball
from blocks import BlockArray


global running
running = True
clock = pygame.time.Clock()



# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Break Out")

# Create game objects
paddle = Paddle(screen, PADDLE_WIDTH, PADDLE_HEIGHT, WHITE)
ball = Ball(screen, BALL_RADIUS, BLUE, (SCREEN_WIDTH//2,SCREEN_HEIGHT - PADDLE_HEIGHT - BALL_RADIUS))
blocks = BlockArray(screen, BLOCK_COLUMNS, BLOCK_ROWS)
blocks.initialize_block_pos()

# Load the background music
pygame.mixer.music.load(MUSIC_FILES[4])
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

def playGame():
    """
    Function to play the game.

    This function handles the game logic, including user input, updating game objects,
    and checking for game over or victory conditions.

    Args:
        None

    Returns:
        None
    """
    global running
    global PADDLE_SPEED
    global SCORE
    
    pass

    # Handle events
    
    # Update paddle position
    
    # Update ball position and check for collisions
    
    # Update score
    
    # Increase paddle speed every frame
    
    
    # Check if the ball has fallen off the screen
    
    # Check if all blocks have been destroyed

    # Clear the screen
    
    # Draw the background

    # Display the score

    # Draw game objects

    # Update the display

def StartGame():
    """
    This function displays the start screen.
    """
    pass
    # Set background color
    
    # Draw the Splash Screen

    # Display a title or instructions

    # Update the display

    # Wait for user input (space key press)
    
    
    # Sets STATE to play to go to playGame

def gameOver():
    """
    This function displays the game over screen.
    """
    pass
    # cleear the screen

    # Draw the Splash Screen
    
    # Display a game over message
     
    # Update the display

    # Wait for user input (R key press)

    # Exit the gameOver function to move to restart state
    
    # Update the display during wait

def won():
    """
    This function displays the game over screen.
    """
    pass
    # Clear the screen
    
    # Draw the Splash Screen

    # Display a game over message
   
    # Update the display

    # Wait for user input (R key press)
    
    # Exit the gameOver function
    # Update the display during wait

def resetGame():
    """
    Resets the game state and initializes the game elements to their default positions and values.
    """
    pass

# Mapping the states to their respective functions
States = {"start": StartGame, "play": playGame, "over": gameOver, "won": won}

# Game Loop
while running:  
    # Cap the frame rate
    clock.tick(60)
    # Call the appropriate function based on the current state
    States[STATE]()


# Quit Pygame
pygame.quit()
