import sys

import pygame

def check_keydown_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
            
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
            
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    

def check_events(ship):
    # 响应鼠标键盘
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(game_settings, screen, ship):
    # 刷新屏幕
    screen.fill(game_settings.bg_color)
    ship.blitme()
    pygame.display.flip()


