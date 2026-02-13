import pygame # type: ignore

pygame.font.init()

class Hud(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        self.x = x
        self.y = y
        self.score = 0
        self.lives = 3
        self.font = pygame.font.Font("/home/snapdragnn/workspace/bootdotdev/asteroids/fonts/SlopeOpera.ttf", 36)

    def increment_score(self, amount):
        self.score += amount

    def update_lives(self, amount):
        self.lives += amount

    def draw(self, screen):
        score_surface = self.font.render(f"Score: {self.score}", True, "white")
        screen.blit(score_surface, (self.x, self.y))

        lives_surface = self.font.render(f"Lives: {self.lives}", True, "white")
        lives_rect = lives_surface.get_rect()
        lives_rect.topright = (screen.get_width() - self.x, self.y)
        screen.blit(lives_surface, lives_rect)
        