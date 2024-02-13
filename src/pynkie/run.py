import pygame as pg
from time import time

import pynkie.events as events
from pynkie.model import Model
import pynkie.debug as debug
from pynkie.view import View

class Pynkie:

    def __init__(self, screen_width: int, screen_height: int) -> None:
        self.views: list[View] = []
        self.models: list[Model] = []
        self.event_listenters: dict[int, list[events.EventListener]] = {}

        self.screen_width: int = screen_width
        self.screen_height: int = screen_height
        self.max_framerate: int = 60
        self.debug_info: bool = False
        self.use_default_cursor: bool = True

        pg.mouse.set_visible(self.use_default_cursor)

        flags: int = pg.HWSURFACE | pg.DOUBLEBUF | pg.RESIZABLE
        self.display: pg.Surface = pg.display.set_mode((self.screen_width, self.screen_height), flags, vsync=1)
        pg.display.set_caption("pynkie project")
        self.display.fill((0, 0, 0))
        self.clock = pg.time.Clock()

    def set_max_framerate(self, max_framerate: int) -> None:
        self.max_framerate = max_framerate

    def set_debug_info(self, debug_info: bool) -> None:
        self.debug_info = debug_info

    def set_use_default_cursor(self, use_default_cursor: bool) -> None:
        self.use_default_cursor = use_default_cursor

    def add_view(self, view: View) -> None:
        self.views.append(view)

    def add_model(self, model: Model) -> None:
        self.models.append(model)

    def add_event_listener(self, event_type: int, event_listener: events.EventListener) -> None:
        if event_type in self.event_listenters.keys():
            self.event_listenters[event_type].append(event_listener)
        else:
            self.event_listenters[event_type] = [event_listener]

    def add_event_listeners(self, event_type: int, event_listeners: list[events.EventListener]) -> None:
        if event_type in self.event_listenters.keys():
            for event_listener in event_listeners:
                self.event_listenters[event_type].append(event_listener)
        else:
            self.event_listenters[event_type] = event_listeners

    def run(self) -> None:
        # run main loop
        self.main_loop()

    def main_loop(self, ) -> None:
        prev_time: float = time()
        dt: float = 0.  # delta time [s]
        while True:
            # handle events
            # update the state of elements based on events/player triggers
            events.handle_events(self.event_listenters)
            
            # update models
            for model in self.models:
                model.update(dt)

            # draw elements
            for view in self.views:
                view.draw(self.display)

            # debug info, blit on top of everything
            if self.debug_info: debug.display_debug(self.display)
            
            # update screen
            pg.display.flip()

            # tick
            self.clock.tick(self.max_framerate)
            
            # delta time
            now: float = time()
            dt: float = now - prev_time
            prev_time = now
            if self.debug_info:
                debug.debug["DT"] = dt
                debug.debug["FPS"] = int(round(1 / dt))