import pygame


class Alien(pygame.sprite.Sprite):
    def __init__(self, color, x, y):  # farbe, und x sowie y Position
        super().__init__()
        file_path = 'graphics/' + color + '.png'  # durch diese Art sind wechselnde Farben möglich
        self.image = pygame.image.load(file_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
