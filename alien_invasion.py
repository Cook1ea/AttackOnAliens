import sys
    
import pygame

def run_game():
    #  初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption("Alien Invasion")
    
    # 背景色
    bg_color = (230, 230, 230)

    # 开始游戏主循环
    while True:
        
        # 给背景上色
        screen.fill(bg_color)

        # 监视鼠标和键盘事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 让最近绘制的屏幕可见
        pygame.display.flip()
    
run_game()

