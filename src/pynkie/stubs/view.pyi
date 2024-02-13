import pygame as pg
from _typeshed import Incomplete
from typing import Any

from pynkie.elements import Element
from pynkie.events import EventListener as EventListener

AnyGroup: Incomplete

class View(AnyGroup, EventListener):
    def __init__(self) -> None: ...

class Viewport:
    camera: pg.Rect
    screen_size: pg.Vector2
    def __init__(self, camera: pg.Rect, screen_size: pg.Vector2) -> None: ...

class ScaledView(View):
    viewport: Viewport
    scale: float
    minimum_dimensions: pg.Vector2
    background: pg.Surface
    view_surface: pg.Surface
    center_element: Element | None = None
    def __init__(self, viewport: Viewport) -> None: ...
    def on_window_resize(self, event: pg.event.Event) -> None: ...
    def recalculate_window_dimensions(self, size: pg.Vector2) -> None: ...
    def on_key_down(self, event: pg.event.Event) -> None: ...
    def center_camera(self) -> None: ...
    def update_viewport(self, new_viewport: Viewport) -> None: ...
    def draw(self, surface: pg.Surface, *args: Any) -> list[pg.Rect]: ...

class StaticView(View):
    def __init__(self) -> None: ...
