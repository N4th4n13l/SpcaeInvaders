import pygame
from laser import Laser


class Player(pygame.sprite.Sprite):  # muss immer so sein um ein Sprite zu generieren
    def __init__(self, pos, constraint, speed):  # wo, max Spielfeldbreite, Geschwindigkeit
        super().__init__()
        self.image = pygame.image.load('graphics/player.png').convert_alpha()  # das Bild
        self.rect = self.image.get_rect(midbottom=pos)  # der Collider des Bild
        self.speed = speed  # Bewegungsgeschwindigkeit
        self.max_x_constraint = constraint  # Horizontale begrenzung max. X-Bewegung

        self.ready = True  # Ready Abfrage für den Laser
        self.laser_time = 0  # Laser
        self.laser_cooldown = 200  # Laser_cooldown damit man nicht einfach darauf bleiben kann

        self.lasers = pygame.sprite.Group()

    def get_input(self):
        keys = pygame.key.get_pressed()  # braucht es immer
        # Zuweisung der Tasten
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        elif keys[pygame.K_a]:
            self.rect.x -= self.speed

        if keys[pygame.K_w]:
            self.rect.y -= self.speed
            if self.rect.y <= 500:
                self.rect.y = 500
        elif keys[pygame.K_s]:
            self.rect.y += self.speed
            if self.rect.y >=570:
                self.rect.y = 570

        #  Laser abfeuern mit cooldown
        if keys[pygame.K_SPACE] and self.ready:
            self.shoot_laser()
            self.ready = False
            self.laser_time = pygame.time.get_ticks()

    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_cooldown:
                self.ready = True

    def constraint(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.max_x_constraint:
            self.rect.right = self.max_x_constraint

    def shoot_laser(self):
        self.lasers.add(Laser(self.rect.center, -10, self.rect.bottom))

    def update(self):
        self.get_input()
        self.constraint()
        self.recharge()
        self.lasers.update()
