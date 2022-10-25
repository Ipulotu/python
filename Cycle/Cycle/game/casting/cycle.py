""" File for the Cycle class of the Cycle game.
    Author: CSE210 - Week 5 Snake game example code.
    Edits by: Ikaika Pulotu (Added another actor.)
              Jordan Greenwood (changed the body symbol from "#" to "u'\U0001F427'"(Penguin emoji))
"""
import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Cycle(Actor):
    """
    A light cycle with light tail.
    
    The responsibility of Cycle is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, color, start):
        """Constructor function inheriting from the Actor class"""
        super().__init__()
        self._segments = []
        self._prepare_body(start)
        self._color = color                # #################### add color & start  ###############

    def get_segments(self):
        """Function for the segments that make up the tail"""
        return self._segments
    
    def set_color(self, color):
        """Function to set the color for the tails."""
        self._color = color

    def move_next(self):
        """move all segments"""
        self._segments[0].move_next()
        self._segments[1].move_next()
        self.grow_tail(1)

        # update velocities
        for i in range(2 - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)
        
    def get_head(self):
        """Function to get the cycle"""
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        """Function for increasing the length of the tail, and symbol used for the tail with color."""
        for i in range(number_of_segments):    # set velocity to Point(0,0) 
            position = self.get_segments()[1].get_position()
            segment = Actor()
            segment.set_position(position)
            segment.set_text("u'\U0001F427'")
            segment.set_color(self._color)
            self._segments.append(segment)

    def turn_head(self, velocity):
        """Function for allowing for cycle movement"""
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self, start):  # ############################ start now required ##############################
        """Function for preparing the start of the game."""                   
        x = int(constants.MAX_X / start)
        y = int(constants.MAX_Y / 2)

        for i in range(constants.CYCLE_LENGTH):
                position = Point(x - i * constants.CELL_SIZE, y)
                velocity = Point(1 * constants.CELL_SIZE, 0)
                text = "@" if i == 0 else "u'\U0001F427'"
                color = self._color

                segment = Actor()
                segment.set_position(position)
                segment.set_velocity(velocity)
                segment.set_text(text)
                segment.set_color(color)
                self._segments.append(segment)