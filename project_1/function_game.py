import sys
import pygame


def check_key_down(ship, event):
    if event.key == pygame.K_d:
        ship.moving_right = True
    if event.key == pygame.K_a:
        ship.moving_left = True
    if event.key == pygame.K_w:
        ship.moving_up = True
    if event.key == pygame.K_s:
        ship.moving_down = True


def check_key_up(ship, event):
    if event.key == pygame.K_d:
        ship.moving_right = False
    if event.key == pygame.K_a:
        ship.moving_left = False
    if event.key == pygame.K_w:
        ship.moving_up = False
    if event.key == pygame.K_s:
        ship.moving_down = False


def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down(ship, event)
        elif event.type == pygame.KEYUP:
            check_key_up(ship, event)


def update_screen(ai_settings, screen, ship):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()
