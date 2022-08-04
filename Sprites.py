import pygame

class TransSprite(pygame.sprite.Sprite):
    def __init__(self, fileName, index):
        super(TransSprite, self).__init__()
        self.surf = pygame.image.load(fileName + str(index) + ".png").convert_alpha()
        self.rect = self.surf.get_rect()