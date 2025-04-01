import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity

    def update(self, dt):
        # Update the position of the shot based on its velocity
        self.position += self.velocity * dt

    def draw(self, screen):
        # Draw the shot as a small circle
        pygame.draw.circle(screen, "white", self.position, self.radius)
