import pygame as pg
from _typeshed import Incomplete as Incomplete

class Element:
    idgen: int
    id: Incomplete
    rect: Incomplete
    def __init__(self, pos: tuple[int, int] = (0, 0), size: tuple[int, int] = (0, 0)) -> None: ...

class SpriteElement(Element, pg.sprite.Sprite):
    image: Incomplete
    def __init__(self, pos: tuple[int, int], img: pg.Surface) -> None: ...
