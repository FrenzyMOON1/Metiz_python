from settings import Settings
from function_game import *
from ship import Ship
from pygame.sprite import Group


def run_game():
    pygame.init()
    pygame.font.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen, ai_settings)
    bullets = Group()

    while True:
        ship.update()
        check_events(ship)
        update_screen(ai_settings, screen, ship)
        check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        update_screen(ai_settings, screen, ship, bullets)


run_game()
