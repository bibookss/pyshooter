import pygame
from constants import PLAYER_HEIGHT, PLAYER_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_SPEED
from bullet import Bullet

class Player():
    def __init__(self, nid, x, y, color):
        self.nid = nid
        self.x = x
        self.y = y
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.color = color
        self.rect = (x, y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.vel = PLAYER_SPEED
        self.bullets = []
        self.can_shoot = True
        self.timer = 50
        self.health = 100

    def shoot(self):
        bullet = Bullet(self.x + self.width // 2, self.y + self.height // 2, self.nid)  # Adjust direction as needed
        self.bullets.append(bullet)
        self.can_shoot = False

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            if self.x - self.vel <= 0:
                return
            if self.nid == 2 and self.x - self.vel <= SCREEN_WIDTH // 2:
                return
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            if self.x + self.vel + self.width >= SCREEN_WIDTH:
                return
            if self.nid == 1 and self.x + self.vel + self.width >= SCREEN_WIDTH // 2:
                return
            self.x += self.vel

        if keys[pygame.K_UP]:
            if self.y - self.vel <= 0:
                return
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            if self.y + self.vel + self.height >= SCREEN_HEIGHT:
                return
            self.y += self.vel

        if keys[pygame.K_SPACE] and self.can_shoot:
            self.shoot()

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
        if not self.can_shoot:
            self.timer -= 1
            if self.timer <= 0:
                self.can_shoot = True
                self.timer = 50

    def collide(self, bullets):
        for bullet in bullets:
            if (self.x < bullet.x < self.x + self.width or
                self.x < bullet.x + bullet.radius < self.x + self.width) and \
               (self.y < bullet.y < self.y + self.height or
                self.y < bullet.y + bullet.radius < self.y + self.height):

                self.health -= bullet.damage
                return bullets.index(bullet)
        return -1