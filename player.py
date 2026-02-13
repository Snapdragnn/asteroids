import pygame # type: ignore
from constants import *
from circleshape import CircleShape
from shot import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.velocity = pygame.Vector2(0, 0)

    def forward(self):
        return pygame.Vector2(0, 1).rotate(self.rotation)

    def triangle(self):
        forward = self.forward()
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]    

    def draw(self, screen):
        points = self.triangle()
        pygame.draw.polygon(screen, "white", points, LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        accel = pygame.Vector2(0, 0)
        forward = self.forward()

        if keys[pygame.K_w]:
            accel += forward * ACCELERATION
        if keys[pygame.K_s]:
            accel -= forward * ACCELERATION

        self.velocity += accel * dt
        self.velocity *= max(0.0, 1.0 - DRAG * dt)
        if self.velocity.length() > MAX_SPEED:
            self.velocity.scale_to_length(MAX_SPEED)
        self.position += self.velocity * dt

        if keys[pygame.K_SPACE]:
            self.shoot()

        self.wrap_position()

    def shoot(self):
        if self.timer > 0:
            pass
        else:
            self.timer = PLAYER_SHOOT_COOLDOWN_SECONDS
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED