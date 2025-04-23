import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    running = True
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    player1 = Player(x, y)
    field = AsteroidField()
    

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return     
        pygame.Surface.fill(screen, (0, 0, 0))
        for  things in drawable:
            things.draw(screen)
        pygame.display.flip()
        updatable.update(dt)
        for roids in asteroids:
            if roids.collide(player1):
                print("Game over!")
                pygame.quit()
                return
        for roids in asteroids:
            for shot in shots:
                if roids.collide(shot):
                    roids.split()
                    shot.kill()
        clock.tick(60)
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()