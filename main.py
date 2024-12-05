# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shots import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    
    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (updatable_group, drawable_group, asteroids_group)
    AsteroidField.containers = (updatable_group)
    Shot.containers = (shots_group, updatable_group, drawable_group)

    AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable_group:
            obj.update(dt)
        
        for asteroid in asteroids_group:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()

            for shot in shots_group:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()

        screen.fill((0,0,0))
        
        for obj in drawable_group:
            obj.draw(screen)

        
        
        pygame.display.flip()
    
        dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()
