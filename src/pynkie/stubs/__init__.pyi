import pynkie as pynkie
from . import debug as debug, elements as elements, events as events, model as model, run as run, view as view

def init(screen_width: int, screen_height: int) -> run.Pynkie: ...

__all__ = ['pynkie', 'debug', 'elements', 'events', 'model', 'run', 'view']
