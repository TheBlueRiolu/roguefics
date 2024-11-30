#!/usr/bin/env python

import tcod.event

class Entity:
    """
An entity in the world.
    """
    
    def __init__(self, sprite: str):
        self.sprite = sprite
        self.x, self.y = 0, 0
        self.active = False

class Prototype:
    """
A prototype used to generate similar entities.
    """
    pass

class Being(Entity):
    """
A mobile entity.

TODO:
- Apply prototypes to characters
    """
    def __init__(self, sprite: str, proto: Prototype):
        super().init(self, self.sprite)

class Player(Being):
    """
The player behaves differently from other beings.
    """
    def update(self, event: tcod.event.KeyboardEvent) -> None:
        if not self.active:
            return
        if (isinstance(event, tcod.event.KeyDown) and
            event.scancode == tcod.event.Scancode.W and
            event.mod == tcod.event.Modifier.NONE):
            self.move(0, -1)
        if (isinstance(event, tcod.event.KeyDown) and
            event.scancode == tcod.event.Scancode.A and
            event.mod == tcod.event.Modifier.NONE):
            self.move(-1, 0)
        if (isinstance(event, tcod.event.KeyDown) and
            event.scancode == tcod.event.Scancode.S and
            event.mod == tcod.event.Modifier.NONE):
            self.move(0, 1)
        if (isinstance(event, tcod.event.KeyDown) and
            event.scancode == tcod.event.Scancode.D and
            event.mod == tcod.event.Modifier.NONE):
            self.move(1, 0)

    def move(x, y):
        """
Move by a vector.
        """
        self.x += x
        self.y += y

class Pickup(Entity):
    """
An item in the world.
    """
    pass

class InventoryItem:
    """
An item in the inventory.
    """
    pass
