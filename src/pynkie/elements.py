import pygame as pg

# element

class Element:

    idgen = 0

    def __init__(self, pos: tuple[int, int]=(0, 0), size: tuple[int, int]=(0, 0)):
        self.id = Element.idgen
        Element.idgen += 1
        self.rect = pg.Rect(pos, size)
        
    def __str__(self):
        return type(self).__name__ + "[id=" + str(self.id) + "]"

# sprite

class SpriteElement(Element, pg.sprite.Sprite):

    def __init__(self, 
                 pos: tuple[int, int], 
                 img: pg.Surface):
        Element.__init__(self, pos, img.get_size())
        pg.sprite.Sprite.__init__(self)
        self.image = img.copy()

