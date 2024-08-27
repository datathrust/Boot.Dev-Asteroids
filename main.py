import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import *
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_running = True
    game_clock = pygame.time.Clock()

    #Pygame update groups:
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)

    field = AsteroidField()
    player_ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    delta_time = 0

    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(delta_time)

        for obj in asteroids:
            if obj.detect_collision(player_ship):
                print('Game over!')
                sys.exit()
        screen.fill("#000000")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        delta_time = game_clock.tick(60) / 1000



if __name__ == '__main__': 
    main()