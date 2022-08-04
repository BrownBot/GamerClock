import pygame
import Sprites

class NumSprite():
    def __init__(self, fileName):
        self.sprites = [Sprites.TransSprite(fileName,i) for i in range(10)]
    def Surface(self,number):
        return self.sprites[number].surf

