import pygame

class GameObject:
    def __init__(self, x, y, width, height, color):
        # Private attributes (encapsulation)
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__color = color
        self.__is_active = True
    
    # Getter methods (encapsulation)
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def get_width(self):
        return self.__width
    
    def get_height(self):
        return self.__height
    
    def get_color(self):
        return self.__color
    
    def is_active(self):
        return self.__is_active
    
    # Setter methods (encapsulation)
    def set_x(self, x):
        self.__x = x
    
    def set_y(self, y):
        self.__y = y
    
    def set_active(self, active):
        self.__is_active = active
    
    def get_rect(self):
        """Mengembalikan rectangle untuk collision detection"""
        return pygame.Rect(self.__x, self.__y, self.__width, self.__height)
    
    def move(self, dx, dy):
        """Method yang akan di-override oleh child classes (polymorphism)"""
        self.__x += dx
        self.__y += dy
    
    def draw(self, screen):
        """Method yang akan di-override oleh child classes (polymorphism)"""
        pygame.draw.rect(screen, self.__color, self.get_rect())
    
    def update(self):
        """Method yang akan di-override oleh child classes (polymorphism)"""
        pass