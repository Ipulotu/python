""" Main file to start the game. The game is run from here.
    Authors: Week 5 Snake game example.
    Edits by: Ikaika Pulotu and Jordan Greenwood
"""
import constants
from game.casting.cast import Cast
from game.casting.powers import Powers
from game.casting.score import Score
from game.casting.cycle import Cycle
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService



def main():
    """ Funtion that creates the cast for the game."""
    cast = Cast()
    cast.add_actor("powers", Powers())                   #  ################### added powers & second cycle/score ####################
    cast.add_actor("cycles", Cycle(constants.CYAN, 4))
    cast.add_actor("cycles", Cycle(constants.ORANGE, 1.5))
    cast.add_actor("scores", Score())
    cast.add_actor("scores", Score())

    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    hca = HandleCollisionsAction()
    script.add_action("input", ControlActorsAction(keyboard_service, hca))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", hca)
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service) 
    director.start_game(cast, script)


if __name__ == "__main__":
    main()