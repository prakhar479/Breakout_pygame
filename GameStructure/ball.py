import pygame
import math
import random
from constants import *


import pygame
import math


class Ball:
    """
    Represents a ball in the game.

    Attributes:
        screen (pygame.Surface): The game screen.
        radius (int): The radius of the ball.
        color (tuple): The color of the ball.
        position (list): The position of the ball.
        velocity (list): The velocity of the ball.
        sprite (pygame.Surface): The sprite of the ball.
    """

    def __init__(self, screen, radius, color, initial_position):
        """
        Initializes a new instance of the Ball class.

        Args:
            screen (pygame.Surface): The game screen.
            radius (int): The radius of the ball.
            color (tuple): The color of the ball.
            initial_position (tuple): The initial position of the ball.
        """
        self.screen = screen
        self.radius = radius
        self.color = color
        # Convert tuple to list for mutable position
        self.position = list(initial_position)
        self.velocity = [0, 0]
        
        sprite = pygame.image.load(BALL_SPRITE)  # Load the sprite
        # Scale the sprite to the ball size
        self.sprite = pygame.transform.scale(sprite, (2*radius, 2*radius))

    def update(self, paddle, block_array):
        """
        Updates the ball's position and velocity.

        Args:
            paddle (Paddle): The paddle object.
            block_array (BlockArray): The block array object.
        """
        pass
        # Update ball position based on velocity
        
        # Reverse direction if ball hits the edge of the screen
        

    def collides_with_paddle(self, paddle):
        """
        Checks if the ball collides with the paddle.

        Args:
            paddle (Paddle): The paddle object.

        Returns:
            bool: True if the ball collides with the paddle, False otherwise.
        """
        pass
        

    def draw(self):
        """
        Draws the ball onto the screen.
        """
        pass
        # Draw the ball onto the screen
         
        # calculate the offset position for the sprite
       