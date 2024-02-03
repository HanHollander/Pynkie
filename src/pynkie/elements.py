import pygame as pg

# element

class Element:

    idgen: int = 0

    def __init__(self, pos: tuple[int, int]=(0, 0), size: tuple[int, int]=(0, 0)) -> None:
        self.id: int = Element.idgen
        Element.idgen += 1
        self.rect: pg.Rect = pg.Rect(pos, size)
        
    def __str__(self):
        return type(self).__name__ + "[id=" + str(self.id) + "]"

# sprite

class SpriteElement(Element, pg.sprite.Sprite):

    def __init__(self, pos: tuple[int, int], img: pg.Surface) -> None:
        Element.__init__(self, pos, img.get_size())
        pg.sprite.Sprite.__init__(self)
        self.image: pg.Surface = img.copy()

