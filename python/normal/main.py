#!/usr/bin/env python
import tcod
import maps
import entity

SCREEN_WIDTH, SCREEN_HEIGHT = 80, 24  # Console width and height in tiles.

START_STATE = 0
TOP_MENU_STATE = 1
DARK_TEXT_STATE = 2
QUIZ_STATE = 3
MAP_STATE = 4
ERROR_STATE = -1

def update(event: tcod.event.KeyboardEvent) -> None:
    global state
    for i in entities:
        self.update()
    if state == START_STATE:
        state = TOP_MENU_STATE

def draw(context) -> None:
    global state
    if state == START_STATE:
        with open("resources/title-screen.txt", 'r') as ts:
            console.clear()
            console.print(x=0, y=0, string=ts.read())
            context.present(console)

# Global variables
state = START_STATE
entities = []
current_map = None
console = None

def main() -> None:
    global console
    # Load the font
    tileset = tcod.tileset.load_tilesheet(
        "resources/ibmfont.png", 32, 8, tcod.tileset.CHARMAP_CP437,
    )
    # Create the main console.
    console = tcod.console.Console(SCREEN_WIDTH, SCREEN_HEIGHT, order="F")
    # Create a window based on this console and tileset.
    with tcod.context.new(  # New window for a console of size columns×rows.
        columns=console.width, rows=console.height, tileset=tileset,
    ) as context:
        draw(context)
        while True:  # Main loop, runs until SystemExit is raised.
            console.clear()
            context.present(console)

            # This event loop will wait until at least one event is processed before exiting.
            # For a non-blocking event loop replace `tcod.event.wait` with `tcod.event.get`.
            for event in tcod.event.wait():
                context.convert_event(event)  # Sets tile coordinates for mouse events.
                if not isinstance(event, tcod.event.KeyboardEvent):
                    continue
                print(event) # Print event names and attributes.
                update(event)
                draw(context)
                if isinstance(event, tcod.event.Quit):
                    raise SystemExit()
        # The window will be closed after the above with-block exits.


if __name__ == "__main__":
    main()
