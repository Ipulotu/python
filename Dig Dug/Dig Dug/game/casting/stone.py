"""File for the Stone class in the Dig Dug Game.
   Author: Ikaika Pulotu
   Comments: Jordan Greenwood
"""
import random
import constants
from game.casting.actor import Actor
from game.shared.point import Point

class Stone(Actor):
    """
    A stone that causes issues for the player.
    
    The responsibility of Stone is to select a random position.

    """
    def __init__(self):                             
        """Constructs a level."""
        super().__init__()
        self.set_velocity(Point(0,15))

    def fall(self, cast):
        """Causes the stone to fall if dirt disappears underneath."""
        for i in cast.get_all_actors():
            if self._position.add(self._velocity).equals(i.get_position()):
                self.move_next()
            

    def place_stone(self, levelcast):
        """Stone placement function for the game.""" 
        dirt = levelcast.get_actors('dirt')[random.randint(0, len(levelcast.get_actors('dirt')))]
        self.set_position(dirt.get_position())
        levelcast.remove_actor('dirt', dirt)
        self.set_color(constants.gray)
        self.set_text("O")