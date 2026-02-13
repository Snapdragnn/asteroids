import pygame # type: ignore

class Explosion(pygame.sprite.Sprite):
    containers = ()

    def __init__(self, pos, lifetime=0.35, start_radius=6, end_radius=48, width=3):
        super().__init__(self.containers)
        self.pos = pygame.Vector2(pos)
        self.age = 0.0
        self.lifetime = lifetime
        self.start_radius = start_radius
        self.end_radius = end_radius
        self.width = width

    def update(self, dt):
        self.age += dt
        if self.age >= self.lifetime:
            self.kill()

    def draw(self, screen):
        t = min(self.age / self.lifetime, 1.0)
        radius = self.start_radius + (self.end_radius - self.start_radius) * t
        alpha = int(255 * (1.0 - t))

        size = int(radius * 2 + self.width * 2 + 4)
        surf = pygame.Surface((size, size), pygame.SRCALPHA)

        color = (255, 200, 50, alpha)
        center = (size // 2, size // 2)
        pygame.draw.circle(surf, color, center, int(radius), width=self.width)

        screen.blit(surf, (self.pos.x - size / 2, self.pos.y - size / 2))