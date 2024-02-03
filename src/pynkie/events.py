import pygame as pg

class EventListener:
    def __init__(self) -> None:
        pass

    def handle_event(self, event: pg.event.Event) -> None:
        pass

def handle_events(event_listenters: dict[int, list[EventListener]]) -> None:
    for event in pg.event.get():
        if event.type in event_listenters.keys():
            for event_listener in event_listenters[event.type]:
                event_listener.handle_event(event)