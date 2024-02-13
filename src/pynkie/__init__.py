import pynkie
from . import debug
from . import elements
from . import events
from . import model
from . import run
from . import view

def init(screen_width: int, screen_height: int) -> run.Pynkie:
        return run.Pynkie(screen_width, screen_height)

__all__: list[str] = ["pynkie", "debug", "elements", "events", "model", "run", "view"]




        