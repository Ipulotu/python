""" File for the Powers class for the Cycle game.
    Author: CSE210 - Week 5 Snake game code. 
    Edits by: Ikaika Pulotu (Edits with green comments)
"""
import random
import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Powers(Actor):
    """
    A tasty item that snakes like to eat.
    
    The responsibility of Food is to select a random position and points that it's worth.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):                                # ####################### Removed points ###################################
        "Constructs a new Food."
        super().__init__()
        self.set_text("@")
        self.set_color(constants.YELLOW)
        self.reset()
        
    def reset(self):
        """Selects a random position and points that the food is worth."""
        self._points = random.randint(1, 8)
        x = random.randint(1, constants.COLUMNS - 1)
        y = random.randint(1, constants.ROWS - 1)
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)
        self.set_position(position)
        
