import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

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

    def draw(self, screen : pygame.surface.Surface):
        # sub-classes must override
        pass

    def update(self, dt : int):
        # sub-classes must override
        pass

    #check if position exceeds any screen boundaries and if so, show up on the other side 
    def wrapAround(self):
        pass
    
    #This checks collision for all objects in our game
    def checkCollision(self, other_object):
        distance = self.position.distance_to(other_object.position)
        combined_radius = self.radius + other_object.radius
        if distance <= combined_radius:
            return True
        else:
            return False
