import pygame
import math


class Ball:
    def __init__(self, screen, radius, color, initial_position):
        self.screen = screen
        self.radius = radius
        self.color = color
        self.position = list(initial_position)  # Convert tuple to list for mutable position
        self.velocity = [0, 0]  # Random initial velocity

    def update(self, paddle, block_array):
        # Update ball position based on velocity
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        
        self.velocity[0]*=1.0005
        self.velocity[1]*=1.0005
        # Reverse direction if ball hits the edge of the screen
        if self.position[0] < self.radius or self.position[0] > self.screen.get_width() - self.radius:
            self.velocity[0] = -self.velocity[0]
        if self.position[1] < self.radius:
            self.velocity[1] = -self.velocity[1]

        if self.collides_with_paddle(paddle):
            self.velocity[1] = -self.velocity[1]
        
        dir,orient = block_array.update(self)
        self.velocity[dir]*=orient
        


    def collides_with_paddle(self, paddle):
        paddle_rect = paddle.rect
        ball_center = (self.position[0], self.position[1])
        
        closest_x = max(paddle_rect.left, min(ball_center[0], paddle_rect.right))
        closest_y = max(paddle_rect.top, min(ball_center[1], paddle_rect.bottom))

        distance = math.sqrt((ball_center[0] - closest_x) ** 2 + (ball_center[1] - closest_y) ** 2)

        return distance <= self.radius

    def draw(self):
        # Draw the ball onto the screen
        pygame.draw.circle(self.screen, self.color, (int(self.position[0]), int(self.position[1])), self.radius)


