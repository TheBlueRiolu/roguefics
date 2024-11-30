#!/usr/bin/env python

class Map:
    """
A floor in a dungeon, or an overworld area.

Attributes:

    title: The area's name.
    floor: The integer representation of the floor index, or 0 if overworld.
    content: The terrain of the area.
    """
    
    def __init__(self, title: str, floor=0, *, width=56, height=32) -> None:
        m = []
        m.append('H'*width)
        m.append('H' + '#'*(width-2) + 'H')
        for i in range(0, height-4):
            m.append('H' + '#' + ' '*(width-4) + '#' + 'H')
        m.append('H' + '#'*(width-2) + 'H')
        m.append('H'*width)
        self.title = title
        self.floor = floor
        self.content = m

    def __str__(self):
        """
Returns the dungeon name and floor index.

If the floor is 0, it is assumed to be the overworld.
        """
        if self.floor == 0:
            return self.title
        return self.title + " - " + self.floor_name()

    def floor_name(self) -> str:
        """
Returns the floor index.

If the floor is 0, it is assumed to be the overworld.
        """
        if self.floor < -10:
            return 'B' + str(-self.floor) + 'F'
        if self.floor < 0:
            return "B0" + str(-self.floor) + 'F'
        if self.floor > 10:
            return str(self.floor) + 'F'
        if self.floor > 0:
            return '0' + str(self.floor) + 'F'
        return ''
    
    def terrain(self, x: int, y: int) -> str:
        """
Returns the terrain of the area at a given point.
        """
        return self.content[y][x]

    def cell(self, x, y) -> str:
        """
Returns what is visible in the area at a given point.
        """
        if x < 0 or x >= self.width():
            return ' '
        if y < 0 or y >= self.height():
            return ' '
        for i in entities:
            if self.terrain(x, y) in "H#":
                return '#'
            if i.x == x and i.y == y:
                return i.sprite
        return self.terrain(x, y)

    def width(self) -> int:
        """
Returns the width of the map.
        """
        w = len(self.content[0])
        if len(self.content) == 1:
            return w
        for i in self.content[1:]:
            if len(i) != w:
                raise IndexError("Map isn't rectangular")
        return w

    def height(self) -> int:
        """
Returns the height of the map.
        """
        h = len(self.content)
        # Check width
        self.width()
        return h

    def cam(self, x, y, r) -> int:
        """
Returns a view from a specified point and with a specified radius.

Recommended radii are 1, 2, and 10.
        """
        min_x = x - r
        min_y = y - r
        max_x = x + r
        max_y = y + r
        view = []
        for i in range(min_y, max_y+1):
            view.append('')
            for j in range(min_x, max_x+1):
                view[-1] += self.cell(j, i)
        return view

def main() -> None:
    """
Run this program as a script if you would like to test things.
    """

    global DummyEntity, entities

    class DummyEntity:
        """
This is a basic entity-like class used for testing purposes.
        """
        def __init__(self, sprite: str, x: int, y: int):
            self.sprite, self.x, self.y = sprite, x, y

    entities = []
    
    print("IT IS BEST TO RUN THIS FROM A CONSOLE LIKE IDLE, NOT EXECUTE THIS")
    print("AS ITS OWN SCRIPT. IN THE EVENT THAT YOU'RE RUNNING THIS FROM A")
    print("CONSOLE, WE HAVE PROVIDED A BLANK ENTITY LIST AS PROTECTION. IF YOU")
    print("NEED TO POPULATE IT WITH ENTITIES, WE HAVE A DUMMY ENTITY CLASS AT")
    print("'DummyEntity .'")

if __name__ == "__main__":
    main()
