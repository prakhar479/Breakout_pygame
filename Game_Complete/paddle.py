import pygame
from constants import *

class Paddle:
    """
    Represents a paddle in the game.

    Attributes:
    - screen: The game screen surface.
    - width: The width of the paddle.
    - height: The height of the paddle.
    - color: The color of the paddle.
    - rect: The rectangular surface representing the paddle.
    - speed: The movement speed of the paddle.
    """

    def __init__(self, screen, width, height, color):
        """
        Initializes a new instance of the Paddle class.

        Parameters:
        - screen: The game screen surface.
        - width: The width of the paddle.
        - height: The height of the paddle.
        - color: The color of the paddle.
        """
        self.screen = screen
        self.width = width
        self.height = height
        self.color = color

        # Create the rectangular surface
        self.rect = pygame.Rect(1100//2, SCREEN_HEIGHT - 30, self.width, self.height)
        self.rect.bottom = self.screen.get_height()  # Position at the bottom of the screen

        # Movement attributes
        self.speed = 0  # Adjust as needed for desired speed
        sprite = pygame.image.load(PADDLE_SPRITE)
        self.sprite = pygame.transform.scale(sprite, (self.width, self.height))

    def update(self):
        """
        Updates the position of the paddle based on its speed.

        This method is called every frame to update the paddle's position.
        """
        # Move the sprite horizontally
        self.rect.x += self.speed
        self.speed *= 1.005

        # Check boundaries to keep sprite within the screen
        if self.rect.right > self.screen.get_width():
            self.rect.right = self.screen.get_width()
            self.speed = 0  # Reverse direction when hitting the right edge
        elif self.rect.left < 0:
            self.rect.left = 0
            self.speed = 0  # Reverse direction when hitting the left edge

    def draw(self):
        """
        Draws the paddle onto the game screen.

        This method is called every frame to draw the paddle onto the screen.
        """
        # Draw the rectangular sprite onto the screen
        # pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.sprite, self.rect)

