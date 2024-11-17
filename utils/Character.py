import pygame
from utils.Constants import *
from utils.ColorUtils import RED

class Player:
    def __init__(self, x = SCREEN_WIDTH // 2, y = SCREEN_HEIGHT // 2, width = 20, height = 50, color = RED, speed = 10, gravity = GRAVITY):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        self.gravity = gravity
        self.velocity_y = 0
        self.on_floor = False
        self.on_platform = False
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, keys):
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed

        # Apply gravity
        if not self.on_floor or not self.on_platform:
            self.velocity_y += self.gravity
            self.rect.y += self.velocity_y

        # Edge checks
        if self.rect.left < 0: # Left
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH: # Right
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0: # Top
            self.rect.top = 0


    def jump(self):
        if self.on_floor or self.on_platform:
            self.velocity_y = -15
            self.on_floor, self.on_platform = False, False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)