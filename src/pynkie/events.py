import sys
import pygame as pg

class EventListener:
    def __init__(self) -> None:
        pass

    def handle_event(event: pg.event.Event):
        pass

def handle_events(event_listenters: dict[int, list[EventListener]]):
    for event in pg.event.get():
        if event.type in event_listenters.keys():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEMOTION:
                for event_listener in event_listenters[event.type]:
                    event_listener.on_mouse_motion(event)

            if event.type == pg.KEYDOWN:
                for event_listener in event_listenters[event.type]:
                    event_listener.on_key_down(event)

            if event.type == pg.KEYUP:
                for event_listener in event_listenters[event.type]:
                    event_listener.on_key_up(event)
            
            if event.type == pg.VIDEORESIZE:
                for event_listener in event_listenters[event.type]:
                    event_listener.on_window_resize(event)