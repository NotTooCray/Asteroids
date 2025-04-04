import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pass


    def update(self, dt):
        # must override
        pass

    def collides_with(self, other):
        # Calculate the distance between the two shapes
        distance = self.position.distance_to(other.position)
        # Check if the distance is less than the sum of their radii
        return distance < (self.radius + other.radius)
