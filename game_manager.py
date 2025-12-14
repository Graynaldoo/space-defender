import pygame
import random
from player import Player
from enemy import Asteroid, FastEnemy

class GameManager:
    def __init__(self, screen_width, screen_height):
        self.__screen_width = screen_width
        self.__screen_height = screen_height
        self.__player = None
        self.__enemies = []
        self.__score = 0
        self.__game_state = "MENU"  # MENU, PLAYING, GAME_OVER
        self.__spawn_timer = 0
        self.__spawn_delay = 1000  # milliseconds
        self.__wave = 1
        
        # Initialize font
        pygame.font.init()
        self.__font = pygame.font.Font(None, 36)
        self.__small_font = pygame.font.Font(None, 24)
    
    def start_game(self):
        """Memulai game baru"""
        self.__player = Player(375, 500)
        self.__enemies = []
        self.__score = 0
        self.__game_state = "PLAYING"
        self.__wave = 1
    
def spawn_enemy(self):
    """Spawn enemy baru berdasarkan wave"""
    current_time = pygame.time.get_ticks()
    
    if current_time - self.__spawn_timer >= self.__spawn_delay:
        x = random.randint(20, self.__screen_width - 60)
        y = random.randint(-100, -50)
        
        # 70% chance asteroid, 30% chance fast enemy
        if random.random() < 0.7:
            enemy = Asteroid(x, y)
        else:
            enemy = FastEnemy(x, y)
        
        self.__enemies.append(enemy)
        self.__spawn_timer = current_time
        
        # Increase difficulty
        if len(self.__enemies) % 5 == 0:
            self.__spawn_delay = max(400, self.__spawn_delay - 50)
    
    def check_collisions(self):
        """Cek collision antara bullets dan enemies, serta player dan enemies"""
        if not self.__player:
            return
        
        # Check bullet-enemy collision
        for bullet in self.__player.get_bullets():
            if not bullet.is_active():
                continue
                
            for enemy in self.__enemies[:]:
                if not enemy.is_active():
                    continue
                    
                if bullet.get_rect().colliderect(enemy.get_rect()):
                    bullet.set_active(False)
                    enemy.set_active(False)
                    self.__player.add_score(enemy.get_points())
                    self.__enemies.remove(enemy)
                    break
        
        # Check player-enemy collision
        player_rect = self.__player.get_rect()
        for enemy in self.__enemies[:]:
            if not enemy.is_active():
                continue
                
            if player_rect.colliderect(enemy.get_rect()):
                self.__player.take_damage(20)
                enemy.set_active(False)
                self.__enemies.remove(enemy)
                
                if self.__player.get_health() <= 0:
                    self.__game_state = "GAME_OVER"
    
    def update(self):
        """Update game logic"""
        if self.__game_state != "PLAYING":
            return
        
        # Update player
        if self.__player:
            self.__player.update()
        
        # Update enemies
        for enemy in self.__enemies[:]:
            enemy.update()
            if not enemy.is_active():
                self.__enemies.remove(enemy)
        
        # Spawn new enemies
        self.spawn_enemy()
        
        # Check collisions
        self.check_collisions()
    
    def handle_input(self, keys):
        """Handle player input"""
        if self.__game_state == "PLAYING" and self.__player:
            dx = 0
            dy = 0
            
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                dx = -1
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                dx = 1
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                dy = -1
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                dy = 1
            if keys[pygame.K_SPACE]:
                self.__player.shoot()
            
            self.__player.move(dx, dy)
    
    def draw(self, screen):
        """Draw semua elemen game"""
        if self.__game_state == "MENU":
            self.__draw_menu(screen)
        elif self.__game_state == "PLAYING":
            self.__draw_game(screen)
        elif self.__game_state == "GAME_OVER":
            self.__draw_game_over(screen)
    
    def __draw_menu(self, screen):
        """Draw menu screen"""
        title = self.__font.render("SPACE DEFENDER", True, (255, 255, 255))
        instruction1 = self.__small_font.render("Press ENTER to Start", True, (200, 200, 200))
        instruction2 = self.__small_font.render("Arrow Keys / WASD to Move", True, (150, 150, 150))
        instruction3 = self.__small_font.render("SPACE to Shoot", True, (150, 150, 150))
        
        screen.blit(title, (self.__screen_width // 2 - title.get_width() // 2, 200))
        screen.blit(instruction1, (self.__screen_width // 2 - instruction1.get_width() // 2, 300))
        screen.blit(instruction2, (self.__screen_width // 2 - instruction2.get_width() // 2, 350))
        screen.blit(instruction3, (self.__screen_width // 2 - instruction3.get_width() // 2, 380))
    
    def __draw_game(self, screen):
        """Draw gameplay screen"""
        # Draw player
        if self.__player:
            self.__player.draw(screen)
        
        # Draw enemies
        for enemy in self.__enemies:
            enemy.draw(screen)
        
        # Draw HUD
        if self.__player:
            score_text = self.__small_font.render(f"Score: {self.__player.get_score()}", True, (255, 255, 255))
            health_text = self.__small_font.render(f"Health: {self.__player.get_health()}", True, (255, 255, 255))
            
            screen.blit(score_text, (10, 10))
            screen.blit(health_text, (10, 40))
            
            # Health bar
            pygame.draw.rect(screen, (255, 0, 0), (10, 70, 200, 20))
            pygame.draw.rect(screen, (0, 255, 0), (10, 70, self.__player.get_health() * 2, 20))
    
    def __draw_game_over(self, screen):
        """Draw game over screen"""
        game_over = self.__font.render("GAME OVER", True, (255, 0, 0))
        final_score = self.__small_font.render(f"Final Score: {self.__player.get_score()}", True, (255, 255, 255))
        restart = self.__small_font.render("Press ENTER to Restart", True, (200, 200, 200))
        
        screen.blit(game_over, (self.__screen_width // 2 - game_over.get_width() // 2, 200))
        screen.blit(final_score, (self.__screen_width // 2 - final_score.get_width() // 2, 280))
        screen.blit(restart, (self.__screen_width // 2 - restart.get_width() // 2, 350))
    
    def get_game_state(self):
        return self.__game_state
    
    def set_game_state(self, state):
        self.__game_state = state