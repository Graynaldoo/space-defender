import pygame
import random
from game_object import GameObject

class Enemy(GameObject):
    def __init__(self, x, y, width, height, color, speed, points):
        super().__init__(x, y, width, height, color)
        self._speed = speed  # Protected attribute
        self._points = points  # Protected attribute
    
    def get_points(self):
        return self._points
    
    def move(self, dx, dy):
        self.set_y(self.get_y() + self._speed)
        
        # Deactivate jika keluar dari screen
        if self.get_y() > 600:
            self.set_active(False)
    
    def update(self):
        """Override method update (POLYMORPHISM)"""
        self.move(0, 1)
    
    def draw(self, screen):
        """Method dasar untuk drawing - akan di-override oleh child classes"""
        pygame.draw.rect(screen, self.get_color(), self.get_rect())


class Asteroid(Enemy):
    def __init__(self, x, y):
        # Asteroid besar
        super().__init__(x, y, 40, 40, (150, 75, 0), 2, 10)
        self.__rotation = 0
        self.__rotation_speed = random.randint(1, 5)
    
    def update(self):
        """Override method update dengan behavior khusus (POLYMORPHISM)"""
        super().update()
        self.__rotation += self.__rotation_speed
    
    def draw(self, screen):
        center_x = self.get_x() + self.get_width() // 2
        center_y = self.get_y() + self.get_height() // 2
        
        # Gambar asteroid sebagai polygon tidak beraturan
        points = [
            (center_x - 20, center_y - 10),
            (center_x - 15, center_y - 20),
            (center_x + 5, center_y - 20),
            (center_x + 20, center_y - 5),
            (center_x + 15, center_y + 15),
            (center_x - 5, center_y + 20),
            (center_x - 20, center_y + 10)
        ]
        pygame.draw.polygon(screen, self.get_color(), points)
        
        # Gambar detail asteroid
        pygame.draw.circle(screen, (100, 50, 0), (center_x - 5, center_y - 5), 4)
        pygame.draw.circle(screen, (100, 50, 0), (center_x + 8, center_y + 5), 3)


class FastEnemy(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y, 30, 30, (255, 0, 0), 4, 20)
        self.__direction = 1  # 1 untuk kanan, -1 untuk kiri
    
    def update(self):
        # Gerak ke bawah
        self.set_y(self.get_y() + self._speed)
        
        # Gerak horizontal zigzag
        self.set_x(self.get_x() + self.__direction * 2)
        
        # Ubah direction jika mencapai boundary
        if self.get_x() <= 0 or self.get_x() >= 770:
            self.__direction *= -1
        
        # Deactivate jika keluar dari screen
        if self.get_y() > 600:
            self.set_active(False)
    
    def draw(self, screen):
        center_x = self.get_x() + self.get_width() // 2
        center_y = self.get_y() + self.get_height() // 2
        
        # Body UFO
        pygame.draw.ellipse(screen, self.get_color(), 
                          (self.get_x(), center_y, self.get_width(), 15))
        
        # Dome UFO
        pygame.draw.arc(screen, (255, 100, 100), 
                       (self.get_x() + 5, self.get_y(), 20, 20), 0, 3.14, 2)
        
        # Lights
        pygame.draw.circle(screen, (255, 255, 0), (self.get_x() + 8, center_y + 5), 2)
        pygame.draw.circle(screen, (255, 255, 0), (self.get_x() + 22, center_y + 5), 2)