""" File for the MoveActorsAction Class.
    This is a child class of the Action class.
    Author: CSE210 Week 5 Snake game code example.
    Edits by: Ikaika Pulotu
              Jordan Greenwood
"""
from game.scripting.action import Action


class MoveActorsAction(Action):
    """
    An update action that moves all the actors.
    
    The responsibility of MoveActorsAction is to move all the actors that have a velocity greater
    than zero.
    """

    def execute(self, cast, script):
        """Executes the move actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        cycles = cast.get_actors("cycles")   # ################# added both cycles &  ###########################
        cycles[0].move_next()
        cycles[1].move_next()