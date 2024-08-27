import pygame
import player
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_status = True
    game_clock = pygame.time.Clock()
    delta_time = 0

    player_ship = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while game_status:
        # Respond to window closure
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #Setup basic background:
        screen.fill('#000000')
        player_ship.draw(screen)
        pygame.display.flip()
        
        dt = game_clock.tick(60) / 1000
    # print(f"Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == '__main__': 
    main()