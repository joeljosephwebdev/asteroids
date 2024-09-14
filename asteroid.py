import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x : int, y: int, radius: int):
        super().__init__(x, y, radius)

    def draw(self, screen : pygame.surface.Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt : int):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20,50)
        piece1_angle = self.velocity.rotate(random_angle)
        piece2_angle = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y,new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y,new_radius)

        asteroid1.velocity = piece1_angle * 1.2
        asteroid2.velocity = piece2_angle * 1.2
        