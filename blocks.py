import pygame

class BlockArray:
    def __init__(self, screen, num_blocks, block_width=35, block_height=20, block_spacing=5):
        self.screen = screen
        self.num_blocks = num_blocks
        self.block_width = block_width
        self.block_height = block_height
        self.block_spacing = block_spacing

    def initialize_block_pos(self):
        x = (self.screen.get_width() - self.num_blocks * (self.block_width + self.block_spacing)) // 2
        y = 50  # Top margin for the blocks
        self.block_pos = []
        for i in range(self.num_blocks):
            # Calculate position of each block
            block_x = x + i * (self.block_width + self.block_spacing)
            block_y = y
            self.block_pos.append((block_x,block_y))


    def draw_blocks(self):
        x = (self.screen.get_width() - self.num_blocks * (self.block_width + self.block_spacing)) // 2
        y = 50  # Top margin for the blocks

        for i in range(self.num_blocks):
            # Calculate position of each block
            block_x = self.block_pos[i][0]
            block_y = self.block_pos[i][1]

            # Draw block
            pygame.draw.rect(self.screen, (255, 0, 0), (block_x, block_y, self.block_width, self.block_height))

    def update(self):
        # Optionally, you can add update logic here if needed
        pass

