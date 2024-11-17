import pygame
from pyautogui import position
from sys import exit as CloseWindow

from pygame.event import event_name

from utils.Constants import *
from utils.ColorUtils import ( WHITE )
from utils.Character import Player
from utils.Scene import (Floor, PlatformManager, PlatformStructure, DrawLevel)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("imthedps")

PlayerCharacter = Player()
MainFloor = Floor()
Platforms = PlatformManager()
PlatformProperties = PlatformStructure(1,1)
Level = DrawLevel(1, 5)


def display_text(text, x, y, font_size = 30, color=(0, 0, 0)):
    # Create a font object
    font = pygame.font.Font(None, font_size)  # Use default font

    # Render the text (anti-aliased, text, color)
    text_surface = font.render(text, True, color)

    # Get the rectangle of the text surface
    text_rect = text_surface.get_rect()

    # Position the rectangle at (x, y)
    text_rect.topleft = (x, y)

    # Blit the text surface onto the screen
    screen.blit(text_surface, text_rect)

run = True
while run:


    for event in pygame.event.get(): # Checks if the user presses the X to close the window
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                PlayerCharacter.jump()
            if event.key == pygame.K_f:
                pass
        if event.type == pygame.MOUSEBUTTONUP and Level.used_platforms < Level.max_platforms:
            mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
            Platforms.add_platform(mouse_pos_x - PlatformProperties.width // 2, mouse_pos_y - PlatformProperties.height // 2)
            Level.used_platforms += 1

    keys = pygame.key.get_pressed()

    PlayerCharacter.move(keys)

    PlayerCharacter.on_floor = False
    PlayerCharacter.on_platform = False

    MainFloor.collision_check(PlayerCharacter)

    if not PlayerCharacter.on_floor:
        Platforms.collision_check(PlayerCharacter)


    screen.fill(WHITE)
    MainFloor.draw(screen)
    Platforms.draw(screen)
    PlayerCharacter.draw(screen)
    Level.draw_goal(screen)

    #display_text(f"On floor: {PlayerCharacter.on_floor}", 100, 100)
    #display_text(f"On platform: {PlayerCharacter.on_platform}", 100, 130)
    display_text(f"Platforms remaining: {Level.max_platforms - Level.used_platforms}", 100, 160)
    display_text(f"{PlayerCharacter.rect.x}", 100, 190)

    pygame.display.flip() # Updates the display every tick
    pygame.time.Clock().tick(60) # 60 FPS


pygame.quit()
CloseWindow()