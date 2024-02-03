import copy
from typing import TYPE_CHECKING, Any
import pygame as pg

import pynkie.elements as elements
from pynkie.events import EventListener

if TYPE_CHECKING:
    AnyGroup = pg.sprite.Group[Any]
else:
    AnyGroup = pg.sprite.Group
class View(AnyGroup, EventListener):

    def __init__(self) -> None:
        AnyGroup.__init__(self)
        EventListener.__init__(self)


class Viewport:

    def __init__(self, camera: pg.Rect, screen_size: pg.Vector2) -> None:
        self.camera: pg.Rect = camera
        self.screen_size: pg.Vector2 = screen_size


class ScaledView(View):
    
    def __init__(self, viewport: Viewport) -> None:
        super().__init__()
        self.viewport: Viewport
        # Smaller is more zoomed in
        self.scale: float = 1
        self.minimum_dimensions: pg.Vector2 = pg.Vector2(viewport.camera.size)
        self.background: pg.Surface
        self.view_surface: pg.Surface
        self.center_element: elements.Element | None = None
        self.update_viewport(viewport)

    def on_window_resize(self, event: pg.event.Event) -> None:
        self._recalculate_window_dimensions(pg.Vector2(event.w, event.h))
    
    def _recalculate_window_dimensions(self, size: pg.Vector2) -> None:
        pref_ratio: float = self.minimum_dimensions.x / self.minimum_dimensions.y
        new_window_ratio: float = size.x / size.y

        new_camera: pg.Rect = copy.copy(self.viewport.camera)
        if new_window_ratio > pref_ratio:
            new_camera.height = round(self.minimum_dimensions.y * self.scale)
            new_camera.width = round(new_camera.height * new_window_ratio)
        else:
            new_camera.width = round(self.minimum_dimensions.x * self.scale)
            new_camera.height = round(new_camera.width / new_window_ratio)
        new_camera.x -= round((new_camera.width - self.viewport.camera.width) / 2)
        new_camera.y -= round((new_camera.height - self.viewport.camera.height) / 2)
    
        self.update_viewport(Viewport(new_camera, size))
    
    def on_key_down(self, event: pg.event.Event) -> None:
        if event.key == pg.K_MINUS:
            self.scale += 0.1
            self._recalculate_window_dimensions(self.viewport.screen_size)
        elif event.key == pg.K_EQUALS:
            self.scale: float = max(0.1, self.scale - 0.1)
            self._recalculate_window_dimensions(self.viewport.screen_size)

    def center_camera(self) -> None:
        if self.center_element is not None:
            self.viewport.camera.x = round(self.center_element.rect.centerx - self.viewport.camera.width / 2)
            self.viewport.camera.y = round(self.center_element.rect.centery - self.viewport.camera.height / 2)


    def update_viewport(self, new_viewport: Viewport) -> None:
        self.viewport = new_viewport
        self.background = pg.Surface(size=self.viewport.camera.size)
        self.background.fill((20, 20, 20))
        self.view_surface = pg.Surface(size=self.viewport.camera.size)

    # override Group.draw
    def draw(self, surface: pg.Surface, *args: Any) -> list[pg.Rect]:
        self.center_camera()

        self.view_surface.blit(self.background, pg.Rect(0, 0, self.viewport.camera.width, self.viewport.camera.height), None, 0)

        for spr in self.sprites():
            if spr.rect.colliderect(self.viewport.camera):
                target_rect = pg.Rect(spr.rect.x - self.viewport.camera.x, spr.rect.y - self.viewport.camera.y,
                                    spr.rect.width, spr.rect.height)
                self.spritedict[spr] = self.view_surface.blit(spr.image, target_rect, None, 0)

        # Scale the view surface to the dimensions of the screen and blit directly
        pg.transform.scale(self.view_surface, self.viewport.screen_size, surface)

        return []

    def __str__(self) -> str:
        return str(type(self)) + ": " + pg.sprite.Group.__str__(self)

class StaticView(View):
    
    def __init__(self) -> None:
        super().__init__()
