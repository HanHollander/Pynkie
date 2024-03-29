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
    def set_max_framerate(self, max_framerate: int) -> None: ...
    def set_debug_info(self, debug_info: bool) -> None: ...
    def set_use_default_cursor(self, use_default_cursor: bool) -> None: ...
    def add_view(self, view: View) -> None: ...
    def add_model(self, model: Model) -> None: ...
    def add_event_listener(self, event_type: int, event_listener: events.EventListener) -> None: ...
    def add_event_listeners(self, event_type: int, event_listeners: list[events.EventListener]) -> None: ...     
    def run(self) -> None: ...
    def main_loop(self) -> None: ...
