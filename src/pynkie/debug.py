from typing import Any
import pygame as pg

font_size: int = 16
font: pg.font.Font = pg.font.Font(None, font_size)
antialias: bool = font_size >= 10

debug: dict[str, Any] = {}
x: int = 0
y0: int = 0

def fmt(v: Any) -> str:
    if isinstance(v, float):
        return "{:.3f}".format(v)
    elif isinstance(v, tuple) or isinstance(v, list) or isinstance(v, pg.Vector2):
        return fmt_listlike(v)
    else:
        return str(v)
    
def fmt_listlike(l: Any) -> str:
    f: str = "["
    if len(l) > 0:
        for v in l:
            f += fmt(v)
            f += ", "
        f = f[:-2]
    f += "]"
    return f

def display_debug(surface: pg.Surface)  -> None:
    i: int = 0
    for (key, value) in debug.items():
        surface.blit(font.render(key + ": " + fmt(value), antialias, (255, 255, 255)), (x, y0 + i * font_size))
        i += 1