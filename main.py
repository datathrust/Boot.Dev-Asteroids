import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_status = True

    while game_status:
        # Respond to window closure
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #Setup basic background:
        screen.fill('#000000')
        pygame.display.flip()
        
    # print(f"Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == '__main__': 
    main()