import pygame # type: ignore
import sys
from constants import *
from logger import log_state, log_event
from hud import *
from shot import *
from player import *
from asteroid import *
from asteroidfield import *
from explosion import *

def main():
    print("Starting Asteroids with pygame version: 2.6.1")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    hud = Hud(10, 10)

    drawable.add(hud)

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    Explosion.containers = (updatable, drawable)
    
    
    AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    lives = 3

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        updatable.update(dt)
        
        for asteroid in asteroids:
            if CircleShape.collides_with(asteroid, player) == True:
                log_event("player_hit")
                lives -= 1
                asteroid.kill()
                hud.update_lives(-1)
                if lives <= 0:
                    print("Game over!")
                    sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if CircleShape.collides_with(asteroid, shot) == True:
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
                    hud.increment_score(1)
                    Explosion(asteroid.position)
        
        for draw in drawable:
            draw.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()