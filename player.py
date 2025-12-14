import pygame
from game_object import GameObject
from bullet import Bullet

class Player(GameObject):
    def __init__(self, x, y):
        # Memanggil constructor parent class
        super().__init__(x, y, 50, 40, (0, 255, 0))
        self.__speed = 5
        self.__health = 100
        self.__score = 0
        self.__bullets = []
        self.__last_shoot_time = 0
        self.__shoot_cooldown = 300  # milliseconds
    
    # Getter methods khusus untuk Player
    def get_health(self):
        return self.__health
    
    def get_score(self):
        return self.__score
    
    def get_bullets(self):
        return self.__bullets
    
    def add_score(self, points):
        self.__score += points
    
    def take_damage(self, damage):
        """Mengurangi health player"""
        self.__health -= damage
        if self.__health < 0:
            self.__health = 0
    
    def shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.__last_shoot_time >= self.__shoot_cooldown:
            bullet = Bullet(
                self.get_x() + self.get_width() // 2 - 2,
                self.get_y(),
                is_player_bullet=True
            )
            self.__bullets.append(bullet)
            self.__last_shoot_time = current_time
    
    def move(self, dx, dy):
        """
        Override method move dari parent class (POLYMORPHISM)
        Menambahkan boundary checking
        """
        new_x = self.get_x() + dx * self.__speed
        new_y = self.get_y() + dy * self.__speed
        
        # Boundary checking
        if 0 <= new_x <= 750:
            self.set_x(new_x)
        if 0 <= new_y <= 560:
            self.set_y(new_y)
    
    def update(self):
        """Override method update dari parent class (POLYMORPHISM)"""
        # Update semua bullets
        for bullet in self.__bullets[:]:
            bullet.update()
            if not bullet.is_active():
                self.__bullets.remove(bullet)
    
    def draw(self, screen):
        """
        Override method draw dari parent class (POLYMORPHISM)
        Menggambar player sebagai spaceship
        """
        # Body pesawat
        points = [
            (self.get_x() + self.get_width() // 2, self.get_y()),  # Nose
            (self.get_x(), self.get_y() + self.get_height()),      # Left wing
            (self.get_x() + self.get_width(), self.get_y() + self.get_height())  # Right wing
        ]
        pygame.draw.polygon(screen, self.get_color(), points)
        
        # Cockpit
        pygame.draw.circle(screen, (0, 200, 255), 
                         (self.get_x() + self.get_width() // 2, 
                          self.get_y() + self.get_height() // 2), 8)
        
        # Draw bullets
        for bullet in self.__bullets:
            bullet.draw(screen)