"""The Gems class for the Dig Dug game.
   Author edits by: Ikaika Pulotu
   Source code from CSE210 Example program Snake game Week 5
   Comments by: Jordan Greenwood"""
import random
from game.casting.actor import Actor
from game.shared.color import Color

class Gems(Actor):
    """
    Gems for the collector to collect.
    
    The responsibility of Gems is to select a random position.

    """
    def __init__(self):                             
        """Constructs a Gem."""
        super().__init__()
       

    def place_gem(self, levelcast): 
        """Places a new gem."""
        dirt = levelcast.get_actors('dirt')[random.randint(100, len(levelcast.get_actors('dirt')))]
        self.set_position(dirt.get_position())
        levelcast.remove_actor('dirt', dirt)
        r = random.randint(1, 255)
        g = random.randint(1, 255)
        b = random.randint(1, 255)
        self.set_color(Color(r,g,b))
        self.set_text("*")