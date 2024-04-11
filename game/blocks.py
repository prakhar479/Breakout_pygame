import pygame
import random
import math
from constants import *  

class BlockArray:
    def __init__(self, screen, num_blocks, lines, block_width=55, block_height=35, block_spacing=5):
        self.screen = screen
        self.num_blocks = num_blocks
        self.block_width = block_width
        self.block_height = block_height
        self.block_spacing = block_spacing
        self.lines = lines
        self.n = 0

    def initialize_block_pos(self):
        x = (self.screen.get_width() - self.num_blocks * (self.block_width + self.block_spacing)) // 2
        y = 50  # Top margin for the blocks
        self.block_pos = []
        self.n = 0
        block_width = self.block_width + self.block_spacing
        for _ in range(self.lines):
            y += 40
            for i in range(self.num_blocks):
                # Calculate position of each block

                block_x = x + i * (block_width)
                block_y = y
                k = random.randint(1,10)
                # if(pattern(block_x,block_y)):
                color = random.choice([RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA, ORANGE, PINK, PURPLE,])
                self.block_pos.append((block_x,block_y,color))
                self.n+=1


    def draw_blocks(self):

        for i in range(self.n):
            # Calculate position of each block
            block_x = self.block_pos[i][0]
            block_y = self.block_pos[i][1]
            color = self.block_pos[i][2]

            # Draw block
            pygame.draw.rect(self.screen, color, (block_x, block_y, self.block_width, self.block_height))

    def update(self, ball):
        # n = len(self.block_pos)
        for i in range(self.n):

            block_x, block_y, _ = self.block_pos[i]
            if self.is_ball_colliding_with_block(ball, block_x, block_y):
                
                ball_center = (ball.position[0], ball.position[1])

                closest_x = max(block_x, min(ball_center[0], block_x + self.block_width))
                closest_y = max(block_y, min(ball_center[1], block_y + self.block_height))
                self.n-=1
                del self.block_pos[i]
                k = random.randint(0,1)
                
                pygame.mixer.music.load(MUSIC_FILES[k])

                    # Play the current song
                pygame.mixer.music.play()
                # Determine the side of the block where the collision occurred
                if closest_x == block_x or closest_x == block_x + self.block_width:
                    return 0,-1
                elif closest_y == block_y or closest_y == block_y + self.block_height:
                    return 1, -1
                else: return 1, -1
                break
                
        return 0,1

    def is_ball_colliding_with_block(self, ball, block_x, block_y):
        # Calculate the center of the ball
        ball_center = (ball.position[0], ball.position[1])
        # Calculate closest point on block to the ball's center
        closest_x = max(block_x, min(ball_center[0], block_x + self.block_width))
        closest_y = max(block_y, min(ball_center[1], block_y + self.block_height))
        # Calculate distance between ball's center and closest point on block
        distance = math.sqrt((ball_center[0] - closest_x) ** 2 + (ball_center[1] - closest_y) ** 2)
        return distance <= ball.radius

