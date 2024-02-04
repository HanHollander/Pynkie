import pygame as pg
from time import time

import pynkie.events as events
from pynkie.model import Model
import pynkie.setup as setup
import pynkie.debug as debug
from pynkie.view import View

class Pynkie:

    def __init__(self, views: list[View], models: list[Model], event_listenters: dict[int, list[events.EventListener]],
                 screen_width: int, screen_height: int, max_framerate: int, debug_info: bool, use_default_cursor: bool) -> None:
        
        self.views: list[View] = views
        self.models: list[Model] = models
        self.event_listenters: dict[int, list[events.EventListener]] = event_listenters

        self.screen_width: int = screen_width
        self.screen_height: int = screen_height
        self.max_framerate: int = max_framerate
        self.debug_info: bool = debug_info
        self.use_default_cursor: bool = use_default_cursor

        # setup mouse
        pg.mouse.set_visible(self.use_default_cursor)

        # setup screen and clock
        self.display = setup.setup_screen(self.screen_width, self.screen_height)
        self.clock = pg.time.Clock()

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