"""The file that holds the constants for the program."""
import random
from game.shared.color import Color
from game.shared.point import Point



COLUMNS = 40
ROWS = 60
CELL_SIZE = 15
MAX_X = 600
MAX_Y = 900
FRAME_RATE = 12
FONT_SIZE = 15
CAPTION = "Dig Dug"
## The line grass will start at(y axis). 
START_LINE = 300
START_POSITION = Point(round(MAX_X / 2), START_LINE-15)

## Stone color
gray = Color(211,211,211)
## Dirt color
BROWN = Color(165,42,42)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)
WHITE = Color(255, 255, 255)

## Number of gems and stones in level 
STONES = random.randint(20, 30)
GEMS = random.randint(7, 15)