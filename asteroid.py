import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, '#FFFFFF', self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            vect_1 = self.velocity.rotate(angle)
            vect_2 = self.velocity.rotate(-angle)
            new_r = self.radius - ASTEROID_MIN_RADIUS
            left_asteroid = Asteroid(self.position[0], self.position[1], new_r)
            left_asteroid.velocity = vect_1 * 1.2
            right_asteroid = Asteroid(self.position[0], self.position[1], new_r)
            right_asteroid.velocity = vect_2 * 1.2