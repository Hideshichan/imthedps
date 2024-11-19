import pygame
from threading import Timer

from utils.ColorUtils import ( BLACK, AQUA, GOLD )
from utils.Constants import ( SCREEN_WIDTH, SCREEN_HEIGHT )

class Floor:
    def __init__(self, x = 0, y = SCREEN_HEIGHT - 50, width = SCREEN_WIDTH, height = 50, color=BLACK):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        # Draw the floor on the screen
        pygame.draw.rect(screen, self.color, self.rect)

    def collision_check(self, player):
        if player.rect.colliderect(self.rect):
            player.on_floor = True
            player.rect.bottom = self.rect.top
            player.velocity_y = 0


class PlatformStructure:
    def __init__(self, x, y, width = 150, height = 20, color = AQUA):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.width = width
        self.height = height

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

class PlatformManager:
    def __init__(self):
        self.platforms = []  # List to store platforms

    def decay(self):
        if self.platforms:
            self.platforms.pop(0) # Removes oldest (index 0)

    def add_platform(self, x, y, width = 150, height = 20, color = AQUA):
        # Create a new platform and add it to the list then kill it after 2s
        platform = PlatformStructure(x, y, width, height, color)
        self.platforms.append(platform)
        Timer(2, self.decay).start()

    def draw(self, screen):
        # Draw all platforms
        for platform in self.platforms:
            platform.draw(screen)

    def collision_check(self, player):
        for platform in self.platforms:
            if player.rect.colliderect(platform.rect) and player.velocity_y >= 0:
                if (player.rect.bottom >= platform.rect.top) and (player.rect.bottom <= platform.rect.bottom): # If the bottom of the player is within the vertical bounds of the platform
                    player.on_platform = True
                    player.rect.bottom = platform.rect.top
                    player.velocity_y = 0



class DrawLevel:
    def __init__(self, level, max_platforms):
        self.LevelNumber = level
        self.max_platforms = max_platforms
        self.used_platforms = 0
        self.color = GOLD

        self.goal_locations = {
            1 : (100, 100),
            2 : (200, 200)
        }

    def get_goal_loc(self):
        return self.goal_locations[self.LevelNumber]

    def update_level(self, new_level):
        self.LevelNumber = new_level

    def draw_goal(self, screen):
        x, y = self.get_goal_loc()
        pygame.draw.rect(screen, self.color, pygame.Rect(x, y, 50, 50))