import sys

import pygame

def check_events(ship):
    # 响应鼠标键盘
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            
            if event.key == pygame.K_LEFT:
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False

            if event.key == pygame.K_LEFT:
                ship.moving_left = False


def update_screen(game_settings, screen, ship):
    # 刷新屏幕
    screen.fill(game_settings.bg_color)
    ship.blitme()
    pygame.display.flip()


