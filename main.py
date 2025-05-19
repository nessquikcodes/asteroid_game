import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group() # all objects that need to be updated
    drawable = pygame.sprite.Group() # all objects that need to be drawn
    asteroids = pygame.sprite.Group() # all asteroids
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        
        screen.fill("black")
        
        for object in drawable:
            object.draw(screen)
            
        pygame.display.flip()
    
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == '__main__':
    main()
    