""" File for the HandleCollisionsAction class. 
    This is a child class of the Action class.
    Author: CSE 210 Week 5 Snake game code example.
    Edits by: Ikaika Pulotu
              Jordan Greenwood

"""
import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when one cycle collides
    with the food, or the cycle collides with its tail or the other players tail, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self.count1 = 0
        self.count2 = 0

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_power_collision(cast, script)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast, script)

    def _handle_power_collision(self, cast, script):
        """Updates the score nd moves the food if the cycle collides with the power up.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        power = cast.get_first_actor("powers")
        cycles = cast.get_actors("cycles")       #  ################### added second cycle & power_up collision ###########################
        head1 = cycles[0].get_head()
        head2 = cycles[1].get_head()
        ctrolAction = script.get_actions("input")

        if head1.get_position().equals(power.get_position()):
            self.count1 += 40
            power.reset()
        if head2.get_position().equals(power.get_position()):
            self.count2 += 40
            power.reset()

        if self.count1 > 0: 
            ctrolAction[0]._power_up1 = 15
            self.count1 -= 1
        else:
            ctrolAction[0]._power_up1 = 0

        if self.count2 > 0:
            ctrolAction[0]._power_up2 = 15
            self.count2 -= 1
        else:
            ctrolAction[0]._power_up2 = 0

    def _handle_segment_collision(self, cast):
        """Sets the game over flag if a cycle collides with a tail.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        scores = cast.get_actors("scores")  #  ######################## Added 2 cycles, heads, & scores ##########################
        cycles = cast.get_actors("cycles")   
        scores[0].set_position(Point(0,0))
        scores[0].set_position(Point(825, 0))
        head1 = cycles[0].get_head()
        head2 = cycles[1].get_head()
        segments = cycles[0].get_segments()[1:]
        for i in (cycles[1].get_segments()[1:]):
            segments.append(i)
        
        for segment in segments:
            if head1.get_position().equals(segment.get_position()):
                scores[0].add_points(1)
                self._is_game_over = True
                
            if head2.get_position().equals(segment.get_position()):
                scores[1].add_points(1)
                self._is_game_over = True

        
    def _handle_game_over(self, cast, script):
        """Shows the 'game over' message and turns the cycles and power up white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """

        if self._is_game_over:
            cycles = cast.get_actors("cycles")    #  @@@@@@@@@@@@@@@@@@@@@ Must add cycles @@@@@@@@@@@@@@@@@@@@@@@@@@@ 
            power = cast.get_first_actor("powers")

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2) 
            position = Point(x, y)

            message = Actor()
            message.set_position(position)
            message._color = constants.RED
            message.set_text("Game Over!"
            "\nPress space to restart.")
            cast.add_actor("messages", message)

            # Color everything white
            for segment in cycles[1].get_segments():
                segment.set_color(constants.WHITE)
            for segment in cycles[0].get_segments():
                segment.set_color(constants.WHITE)
            cycles[0].set_color(constants.WHITE)
            cycles[1].set_color(constants.WHITE)
            power.set_color(constants.WHITE)

            ctrolAction = script.get_actions("input")
            ctrolAction[0]._power_up1 = 0
            ctrolAction[0]._power_up2 = 0
            self.count1 = 0
            self.count2 = 0
       