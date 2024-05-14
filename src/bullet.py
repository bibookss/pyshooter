import pygame
from constants import YELLOW, GREEN, BULLET_DAMAGE, BULLET_SPEED

class Bullet:
    def __init__(self, x, y, player_id):
        self.x = x
        self.y = y
        self.radius = 5  # Adjust as needed
        self.damage = BULLET_DAMAGE
        self.color = YELLOW if player_id == 1 else GREEN
        self.direction = 1 if player_id == 1 else -1
        self.speed = BULLET_SPEED * self.direction

    def draw(self, win):
        self.move()
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.speed