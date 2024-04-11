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
        # Update ball position based on velocity
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

        self.velocity[0] *= FRAME_MULT
        self.velocity[1] *= FRAME_MULT
        # Reverse direction if ball hits the edge of the screen
        if self.position[0] < self.radius or self.position[0] > self.screen.get_width() - self.radius:
            self.velocity[0] = -self.velocity[0]
            pygame.mixer.Sound(MUSIC_FILES[3]).play()
            # pygame.mixer.music.play()
        if self.position[1] < self.radius:
            self.velocity[1] = -self.velocity[1]
            pygame.mixer.Sound(MUSIC_FILES[3]).play()
            # pygame.mixer.music.play()

        if self.collides_with_paddle(paddle):
            self.velocity[1] = -self.velocity[1]
            self.position[1] = 855
            self.velocity[0] += paddle.speed*COLLIDE_MULT
            pygame.mixer.Sound(MUSIC_FILES[2]).play()
            # pygame.mixer.music.play()

        dir, orient = block_array.update(self)
        self.velocity[dir] *= orient

    def collides_with_paddle(self, paddle):
        """
        Checks if the ball collides with the paddle.

        Args:
            paddle (Paddle): The paddle object.

        Returns:
            bool: True if the ball collides with the paddle, False otherwise.
        """
        paddle_rect = paddle.rect
        ball_center = (self.position[0], self.position[1])

        closest_x = max(paddle_rect.left, min(
            ball_center[0], paddle_rect.right))
        closest_y = max(paddle_rect.top, min(
            ball_center[1], paddle_rect.bottom))

        distance = math.sqrt(
            (ball_center[0] - closest_x) ** 2 + (ball_center[1] - closest_y) ** 2)

        return distance <= self.radius

    def draw(self):
        """
        Draws the ball onto the screen.
        """
        # Draw the ball onto the screen
        # pygame.draw.circle(self.screen, self.color, (int(self.position[0]), int(self.position[1])), self.radius)
        # calculate the offset position for the sprite
        offset_pos = (int(self.position[0])-self.radius,
                      int(self.position[1])-self.radius)
        self.screen.blit(self.sprite, offset_pos)
