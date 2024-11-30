#!/usr/bin/env python

import tcod.event

class Entity:
    """
An entity in the world.
    """
    
    def __init__(self, sprite: str):
        self.sprite = sprite
        self.x, self.y = 0, 0

class Prototype:
    """
A prototype used to generate similar entities.
    """

class Being(Entity):
    """
A mobile entity.

TODO:
- Apply prototypes to characters
    """
    def __init__(self, sprite: str, proto: Prototype):
        pass

class Player(Being):
    """
The player behaves differently from other beings.
    """
    def update(self, event: tcod.event.KeyboardEvent) -> None:
        # KeyDown(scancode=Scancode.W, sym=KeySym.w, mod=<Modifier.NONE: 0>)
        pass

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
