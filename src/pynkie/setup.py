import pygame as pg

def setup_screen(width: int, heigth: int) -> pg.Surface:
    flags: int = pg.HWSURFACE | pg.DOUBLEBUF | pg.RESIZABLE
    display: pg.Surface = pg.display.set_mode((width, heigth), flags, vsync=1)
    pg.display.set_caption("gmtk2023test")
    display.fill((0, 0, 0))

    return display
   