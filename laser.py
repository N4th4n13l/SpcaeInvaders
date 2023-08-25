import pygame


class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, speed, screen_height):
        super().__init__()
        self.speed = speed
        self.image = pygame.Surface((5, 10))  # kein Bild nur ein leerer screen mit einem Strich
        self.image.fill('white')
        self.rect = self.image.get_rect(center=pos)
        self.height_y = screen_height


    def destroy(self):
        if self.rect.y <= -50 or self.rect.y >= self.height_y + 50:
            self.kill()


    def update(self):
        self.rect.y += self.speed
        self.destroy()
