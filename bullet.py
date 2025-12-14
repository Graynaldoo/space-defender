import pygame
from game_object import GameObject

class Bullet(GameObject):
    """
    Bullet class - Demonstrasi INHERITANCE dari GameObject
    """
    def __init__(self, x, y, is_player_bullet=True):
        color = (255, 255, 0) if is_player_bullet else (255, 0, 255)
        super().__init__(x, y, 4, 15, color)
        self.__speed = 10 if is_player_bullet else -8
        self.__is_player_bullet = is_player_bullet
    
    def is_player_bullet(self):
        return self.__is_player_bullet
    
    def move(self, dx, dy):
        """
        Override method move (POLYMORPHISM)
        Bullet bergerak vertikal
        """
        self.set_y(self.get_y() - self.__speed)
        
        # Deactivate jika keluar dari screen
        if self.get_y() < -20 or self.get_y() > 620:
            self.set_active(False)
    
    def update(self):
        """Override method update (POLYMORPHISM)"""
        self.move(0, 0)
    
    def draw(self, screen):
        """
        Override method draw (POLYMORPHISM)
        Menggambar bullet sebagai laser
        """
        # Laser beam
        pygame.draw.rect(screen, self.get_color(), self.get_rect())
        
        # Glow effect
        glow_color = (255, 255, 150) if self.__is_player_bullet else (255, 150, 255)
        pygame.draw.rect(screen, glow_color, 
                        (self.get_x() - 1, self.get_y(), 
                         self.get_width() + 2, self.get_height()), 1)