# SPACE INVADERS

import sys
import pygame.sprite
from player import *
import obstacle
from alien import Alien


# Die Klasse welche die ganze Spiellogik beinhaltet
class Game:
    def __init__(self):

        # Player setup mit seinem Bild und Collider
        player_sprite = Player((screen_width / 2, screen_height), screen_width, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        #  Obstacle setup
        self.shape = obstacle.shape
        self.block_size = 6
        self.blocks = pygame.sprite.Group()
        self.obstacle_amount = 4
        self.obstacle_x_positions = [num * (screen_width / self.obstacle_amount) for num in range(self.obstacle_amount)]
        self.create_multi_obstacles(*self.obstacle_x_positions, x_start=screen_width / 14, y_start=460)

        # Alien setup
        self.aliens = pygame.sprite.Group()
        self.alien_setup(rows=6, cols=8)

    def create_obstacle(self, x_start, y_start, offset_x):
        for row_index, row in enumerate(self.shape):
            for col_index, col in enumerate(row):
                if col == 'x':
                    x = x_start + col_index * self.block_size + offset_x
                    y = y_start + row_index * self.block_size
                    block = obstacle.Block(self.block_size, ('red'), x, y)
                    self.blocks.add(block)

    def create_multi_obstacles(self, *offset, x_start, y_start):
        for offset_x in offset:
            self.create_obstacle(x_start, y_start, offset_x)

    # Die Gegner Funktion -- Aliens
    def alien_setup(self, rows, cols, x_distance=60, y_distance=48, x_offset=70, y_offset=100):
        for row_index, row in enumerate(range(rows)): #  1-6 möglich siehe self.alien.setup
            for col_index, col in enumerate(range(cols)): #  1-8 möglich
                x = col_index * x_distance + x_offset
                y = row_index * y_distance + y_offset

                # wahl der unterschiedlichen Farben der Aliens durch enumerate der row's
                if row_index == 0: alien_sprite = Alien('yellow', x, y)
                elif 1 <= row_index <= 2:alien_sprite = Alien('green', x, y)
                else: alien_sprite = Alien('red', x, y)
                self.aliens.add(alien_sprite)

    def run(self):
        # Spieler, Hindernisse, Schüsse und Gegner auf den Bildschirm bringen
        self.player.update()  # Warum das hier ist weis ich auch nicht :-)

        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen)
        self.blocks.draw(screen)
        self.aliens.draw(screen)


if __name__ == '__main__':  # ausführendes Script
    pygame.init()

    screen_width = 600
    screen_height = 600

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Space Invaders')
    clock = pygame.time.Clock()
    game = Game()  # die Game-Klasse aufrufen

    # Die Schleiffernabfrage, ob das Spiel noch läuft
    while True:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill('black')
        game.run()  # die Funktion run der Game-Klasse starten

        pygame.display.update()  # immer wieder alles neu laden, 60-mal pro Sekunde
        clock.tick(60)
