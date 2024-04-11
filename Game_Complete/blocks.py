import pygame
import random
import math
from constants import *  

class BlockArray:
    """
    Represents an array of blocks in the game.

    Attributes:
    - screen: The game screen where the blocks will be drawn.
    - num_blocks: The number of blocks in each line.
    - lines: The number of lines of blocks.
    - block_width: The width of each block.
    - block_height: The height of each block.
    - block_spacing: The spacing between blocks.
    - blocks: A list to store the positions and colors of the blocks.
    - n: The current number of blocks.
    - SPRITES: A list of block sprites.
    - total: The total number of blocks.

    Methods:
    - __init__(self, screen, num_blocks, lines, block_width=55, block_height=35, block_spacing=5): Initializes the BlockArray object.
    - initialize_block_pos(self): Initializes the positions of the blocks.
    - draw_blocks(self): Draws the blocks on the screen.
    - update(self, ball): Updates the state of the blocks based on the ball's position.
    - is_ball_colliding_with_block(self, ball, block_x, block_y): Checks if the ball is colliding with a block.
    """

    def __init__(self, screen, num_blocks, lines, block_width=70, block_height=35, block_spacing=5):
        """
        Initializes the BlockArray object.

        Parameters:
        - screen: The game screen where the blocks will be drawn.
        - num_blocks: The number of blocks in each line.
        - lines: The number of lines of blocks.
        - block_width: The width of each block (default: 55).
        - block_height: The height of each block (default: 35).
        - block_spacing: The spacing between blocks (default: 5).
        """
        self.screen = screen
        self.num_blocks = num_blocks
        self.block_width = block_width
        self.block_height = block_height
        self.block_spacing = block_spacing
        self.lines = lines
        self.blocks = []
        self.n = 0
        self.SPRITES = [pygame.image.load(sprite) for sprite in BLOCK_SPRITES]
        self.total = 0
        # Scale the block sprites to the block size
        for i in range(len(self.SPRITES)):
            self.SPRITES[i] = pygame.transform.scale(self.SPRITES[i], (block_width, block_height))

    def initialize_block_pos(self):
        """
        Initializes the positions of the blocks.
        """
        x = (self.screen.get_width() - self.num_blocks * (self.block_width + self.block_spacing)) // 2
        y = 30  # Top margin for the blocks
        self.n = 0
        self.blocks = []
        block_width = self.block_width + self.block_spacing
        for _ in range(self.lines):
            y += self.block_height + self.block_spacing
            for i in range(self.num_blocks):
                # Calculate position of each block
                block_x = x + i * (block_width)
                block_y = y
                k = random.randint(1,10)
                color = random.choice(self.SPRITES)
                self.blocks.append((block_x,block_y,color))
                self.n += 1
        self.total = self.n

    def draw_blocks(self):
        """
        Draws the blocks on the screen.
        """
        for i in range(self.n):
            # Calculate position of each block
            block_x = self.blocks[i][0]
            block_y = self.blocks[i][1]
            color = self.blocks[i][2]

            # Draw block
            self.screen.blit(color, (block_x, block_y))

    def update(self, ball):
        """
        Updates the state of the blocks based on the ball's position.

        Parameters:
        - ball: The ball object.

        Returns:
        - A tuple representing the direction of the ball after collision with a block.
        """
        for i in range(self.n):
            block_x, block_y, _ = self.blocks[i]
            if self.is_ball_colliding_with_block(ball, block_x, block_y):
                ball_center = (ball.position[0], ball.position[1])
                closest_x = max(block_x, min(ball_center[0], block_x + self.block_width))
                closest_y = max(block_y, min(ball_center[1], block_y + self.block_height))
                self.n -= 1
                del self.blocks[i]
                
                pygame.mixer.Sound(random.choice(MUSIC_FILES[:2])).play()
                
                if closest_x in (block_x, block_x + self.block_width):
                    return 0, -1
                elif closest_y in (block_y, block_y + self.block_height):
                    return 1, -1
                else:
                    return 1, -1
                
        return 0, 1

    def is_ball_colliding_with_block(self, ball, block_x, block_y):
        """
        Checks if the ball is colliding with a block.

        Parameters:
        - ball: The ball object.
        - block_x: The x-coordinate of the block.
        - block_y: The y-coordinate of the block.

        Returns:
        - True if the ball is colliding with the block, False otherwise.
        """
        ball_center = (ball.position[0], ball.position[1])
        closest_x = max(block_x, min(ball_center[0], block_x + self.block_width))
        closest_y = max(block_y, min(ball_center[1], block_y + self.block_height))
        distance = math.sqrt((ball_center[0] - closest_x) ** 2 + (ball_center[1] - closest_y) ** 2)
        return distance <= ball.radius

