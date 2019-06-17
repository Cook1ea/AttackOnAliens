import pygame

from settings import Settings

from ship import Ship

from game_functions import *

def run_game():
    #  初始化游戏并创建一个屏幕对象
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # 创建一艘飞船
    ship = Ship(game_settings, screen)

    # 开始游戏主循环
    while True:
        
        # 监视鼠标和键盘事件
        check_events(ship)

        # 移动飞船
        ship.update()

        # 刷新屏幕
        update_screen(game_settings, screen, ship)

    
run_game()

