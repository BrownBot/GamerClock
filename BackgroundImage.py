import pygame

class Bground(pygame.sprite.Sprite):
    def __init__(self):
        super(Bground, self).__init__()
        self.surf = pygame.image.load("img/GamerClock.png").convert()
        self.rect = self.surf.get_rect()