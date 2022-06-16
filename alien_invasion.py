import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        # 初始化背景设置，让 pygame 能够正确的工作
        pygame.init()
        self.settings = Settings()

        # 创建一个显示窗口，游戏的所有图形元素都将在其中绘制
        # display.set_mode 返回 surface 对象，表示整个窗口
        # self.screen = pygame.display.set_mode((1200, 800)) # 指定窗口大小
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        # 设置背景色
        # self.bg_color = (230, 230, 230) # RGB
    
    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 监视键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # 每次循环都重绘屏幕
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
        
            # 让最近绘制的屏幕可见
            # pygame 每次循环都将绘制一个空屏幕，并擦去就屏幕，使得只有新屏幕可见
            pygame.display.flip()

if  __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()