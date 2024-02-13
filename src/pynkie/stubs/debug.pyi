import pygame as pg
from typing import Any

font_size: int
font: pg.font.Font
antialias: bool
debug: dict[str, Any]
x: int
y0: int

def fmt(v: Any) -> str: ...
def fmt_listlike(l: Any) -> str: ...
def display_debug(surface: pg.Surface) -> None: ...
