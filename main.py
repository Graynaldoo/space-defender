import pygame
import sys
import random
from game_manager import GameManager

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
BG_COLOR = (10, 10, 30)

def main():
    """Main function untuk menjalankan game"""
    # Initialize Pygame
    pygame.init()
    
    # Setup screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Space Defender - UAS PBO")
    
    # Setup clock
    clock = pygame.time.Clock()
    
    # Create game manager
    game_manager = GameManager(SCREEN_WIDTH, SCREEN_HEIGHT)
    
    # Game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if game_manager.get_game_state() == "MENU":
                        game_manager.start_game()
                    elif game_manager.get_game_state() == "GAME_OVER":
                        game_manager.start_game()
                
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        # Get keys pressed
        keys = pygame.key.get_pressed()
        
        # Handle input
        game_manager.handle_input(keys)
        
        # Update game
        game_manager.update()
        
        # Draw background
        screen.fill(BG_COLOR)
        
        # Draw stars background
        for i in range(100):
            random.seed(i)  # Same stars every frame
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT)
            pygame.draw.circle(screen, (255, 255, 255), (x, y), 1)
        
        # Draw game
        game_manager.draw(screen)
        
        # Update display
        pygame.display.flip()
        
        # Cap frame rate
        clock.tick(FPS)
    
    # Quit
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()