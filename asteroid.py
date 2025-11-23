import pygame, random
from logger import log_event
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            first_asteroid_vector = self.velocity.rotate(random_angle)
            second_asteroid_vector = self.velocity.rotate(- random_angle)
            small_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
            first_asteroid = Asteroid(self.position.x, self.position.y, small_asteroid_radius)
            second_asteroid = Asteroid(self.position.x, self.position.y, small_asteroid_radius)
            first_asteroid.velocity = first_asteroid_vector * 1.2
            second_asteroid.velocity = second_asteroid_vector * 1.2