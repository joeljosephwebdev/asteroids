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
    
    def wrapAround(self):
        if self.position.x + self.radius < 0:
            self.position.x = SCREEN_WIDTH
        if self.position.x - self.radius > SCREEN_WIDTH:
            self.position.x = 0

        if self.position.y + self.radius < 0:
            self.position.y = SCREEN_HEIGHT
        if self.position.y - self.radius > SCREEN_HEIGHT:
            self.position.y = 0

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return SCORE_SMALL
        
        random_angle = random.uniform(20,50)
        piece1_angle = self.velocity.rotate(random_angle)
        piece2_angle = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y,new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y,new_radius)

        asteroid1.velocity = piece1_angle * 1.2
        asteroid2.velocity = piece2_angle * 1.2

        if self.radius > 40:
            return SCORE_LARGE

        return SCORE_MEDIUM
