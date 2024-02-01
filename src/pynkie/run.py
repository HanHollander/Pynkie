from dataclasses import dataclass
import pygame as pg
from time import time

import pynkie.events as events
from pynkie.model import Model
import pynkie.setup as setup
import pynkie.debug as debug
from pynkie.view import View

@dataclass()
class Pynkie:
    views: list[View]
    models: list[Model]
    event_listenters: dict[int, list[events.EventListener]]

    screen_width: int = 1920
    screen_height: int = 1080
    max_framerate: int = 60
    debug_info: bool = False
    use_default_cursor: bool = True

    def run(self):
        # setup mouse
        pg.mouse.set_visible(self.use_default_cursor)

        # setup screen and clock
        display = setup.setup_screen(self.screen_width, self.screen_height)
        clock = pg.time.Clock()

        # run main loop
        self.main_loop(display, clock)


    def main_loop(self, display: pg.Surface, clock: pg.time.Clock):
        prev_time = time()
        dt = 0  # delta time [s]
        while True:
            # handle events
            # update the state of elements based on events/player triggers
            events.handle_events(self.event_listenters)
            
            # update models
            for model in self.models:
                model.update(dt)

            # draw elements
            for view in self.views:
                view.draw(display)

            # debug info
            if self.debug_info: debug.display_debug(display)
            
            # update screen
            pg.display.flip()

            # tick
            clock.tick(self.max_framerate)
            
            # delta time
            now = time()
            dt = now - prev_time
            prev_time = now
            if self.debug_info:
                debug.debug["DT"] = dt
                debug.debug["FPS"] = int(round(1 / dt))