import pygame as pg
import pynkie.events as events
from pynkie.model import Model as Model
from pynkie.view import View as View

class Pynkie:
    views: list[View]
    models: list[Model]
    event_listenters: dict[int, list[events.EventListener]]
    screen_width: int
    screen_height: int
    max_framerate: int
    debug_info: bool
    use_default_cursor: bool
    display: pg.Surface
    clock: pg.time.Clock
    def __init__(self, views: list[View], models: list[Model], event_listenters: dict[int, list[events.EventListener]], screen_width: int, screen_height: int, max_framerate: int, debug_info: bool, use_default_cursor: bool) -> None: ...
    def run(self) -> None: ...
    def main_loop(self) -> None: ...
