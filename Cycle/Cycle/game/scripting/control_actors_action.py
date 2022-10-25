""" File for the ControlActorsAction class of the Cycle game.
    Author: CSE210 Week 5 Snake game code.
    Edits by: Ikaika Pulotu
              Jordan Greenwood
"""
import constants
from game.scripting.action import Action
from game.shared.point import Point
from game.casting.cycle import Cycle


class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service, hca):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction1 = Point(constants.CELL_SIZE, 0)
        self._direction2 = Point(constants.CELL_SIZE, 0)
        self._power_up1 = 0
        self._power_up2 = 0
        self._hca = hca

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        
        # Player one   

        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction1 = Point(-constants.CELL_SIZE-self._power_up1, 0)
        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction1 = Point(constants.CELL_SIZE+self._power_up1, 0)
        
        # up
        if self._keyboard_service.is_key_down('w'):
            self._direction1 = Point(0, -constants.CELL_SIZE-self._power_up1)
        
        # down
        if self._keyboard_service.is_key_down('s'):
            self._direction1 = Point(0, constants.CELL_SIZE+self._power_up1)
        
       # Player two                                                            ################## added second cycle controls ##############################

        # left
        if self._keyboard_service.is_key_down('j'):
            self._direction2 = Point(-constants.CELL_SIZE-self._power_up2, 0)
        
        # right
        if self._keyboard_service.is_key_down('l'):
            self._direction2 = Point(constants.CELL_SIZE+self._power_up2, 0)
        
        # up
        if self._keyboard_service.is_key_down('i'):
            self._direction2 = Point(0, -constants.CELL_SIZE-self._power_up2)
        
        # down
        if self._keyboard_service.is_key_down('k'):
            self._direction2 = Point(0, constants.CELL_SIZE+self._power_up2)

        # space 
        if self._keyboard_service.is_key_down('z'):

            # remove old actors 
            for i in cast.get_actors("cycles"):
                cast.remove_actor("cycles", cast.get_first_actor("cycles"))
            for i in cast.get_actors("messages"):    
                cast.remove_actor("messages", cast.get_first_actor("messages"))

            # create new snakes & restart game
            cast.add_actor("cycles", Cycle(constants.CYAN, 4))
            cast.add_actor("cycles", Cycle(constants.ORANGE, 1.5))
            self._hca._is_game_over = False  

            ctrolAction = script.get_actions("input")
            ctrolAction[0]._power_up1 = 0
            ctrolAction[0]._power_up2 = 0
            self._hca.count1 = 0
            self._hca.count2 = 0
        
        cycles = cast.get_actors("cycles")
        cycles[0].turn_head(self._direction1)
        cycles[1].turn_head(self._direction2)