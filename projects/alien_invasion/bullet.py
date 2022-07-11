import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """飞船发射的子弹类"""

    def __init__(self, ai_settings, screen, ship) -> None:
        """飞船所在的位置创造一个子弹类"""
        super().__init__()
        self.screen = screen

        # 在坐标原点(0,0)处创建一个表示子弹的矩形，并设置正确位置
        self.rect = pygame.Rect(
            0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 储存用小数表示子弹位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数
        self.y -= self.speed_factor
        # 更新表示子弹的rect位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)