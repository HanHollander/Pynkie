import pygame as pg

class Element:
    idgen: int
    id: int
    rect: pg.Rect
    def __init__(self, pos: tuple[int, int] = (0, 0), size: tuple[int, int] = (0, 0)) -> None: ...

class SpriteElement(Element, pg.sprite.Sprite):
    image: pg.Surface
    def __init__(self, pos: tuple[int, int], img: pg.Surface) -> None: ...
