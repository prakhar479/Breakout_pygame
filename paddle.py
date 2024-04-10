import pygame

class Paddle:
    def __init__(self, screen, width, height, color):
        self.screen = screen
        self.width = width
        self.height = height
        self.color = color

        # Create the rectangular surface
        self.rect = pygame.Rect(1100//2, 0, self.width, self.height)
        self.rect.bottom = self.screen.get_height()  # Position at the bottom of the screen

        # Movement attributes
        self.speed = 0  # Adjust as needed for desired speed

    def update(self):
        # Move the sprite horizontally
        self.rect.x += self.speed
        self.speed*=1.005

        # Check boundaries to keep sprite within the screen
        if self.rect.right > self.screen.get_width():
            self.rect.right = self.screen.get_width()
            self.speed = 0  # Reverse direction when hitting the right edge
        elif self.rect.left < 0:
            self.rect.left = 0
            print(self.speed)
            self.speed = 0 # Reverse direction when hitting the left edge

    def draw(self):
        # Draw the rectangular sprite onto the screen
        pygame.draw.rect(self.screen, self.color, self.rect)

