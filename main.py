# this allows us to use code from
# the open-source pygame library
# throughout this file
from ast import AST, Assert
import pygame
from pygame.display import update
from asteroid import Asteroid
from asteroidfeild import AsteroidField
from constants import *
from player import Player, Shot
import sys

def main():

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidFeild = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        updatable.update(dt)
        for asteroid in asteroids:
            asteroid.check_collision(player)
            if asteroid.check_collision(player):
                print("Game Over")
                pygame.quit()
                sys.exit()
            for shot in shots:
                if asteroid.check_collision(shot):
                    asteroid.kill()
                    shot.kill()
        pygame.display.flip()
        dt = clock.tick(60)/1000


    # print("Starting Asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
