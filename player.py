import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x : int, y : int):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0

    #The player hitbox is technically a circle, they are displayed as this triangle.
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen : pygame.surface.Surface):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def update(self, dt : int):

        if self.shot_timer > 0:
            self.shot_timer -= dt

        keys = pygame.key.get_pressed()

        if keys[LEFT]:
            self.rotate(-dt)
        if keys[RIGHT]:
            self.rotate(dt)
        if keys[UP]:
            self.move(dt)
        if keys[DOWN]:
            self.move(-dt)
        if keys[SHOOT]:
            self.shoot()
    
    def rotate(self, dt : int):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt : int):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        if self.shot_timer > 0:
            return
        shot = Shot(self.position.x,self.position.y)
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.shot_timer = PLAYER_SHOOT_COOLDOWN
        