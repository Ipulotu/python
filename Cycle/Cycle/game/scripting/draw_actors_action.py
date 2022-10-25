""" File for the DrawActorsAction class of the Cycle game
    Child class of the Action class.
    Author: CSE210 Week 5 Snake game code example.
    Edits by: Ikaika Pulotu
              Jordan Greenwood
"""
from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        scores = cast.get_actors("scores") 
        power = cast.get_first_actor("powers")
        cycles = cast.get_actors("cycles")                     #   ############## added second cycle ###################################
        segments1 = cycles[0].get_segments()
        segments2 = cycles[1].get_segments()
        messages = cast.get_actors("messages")

        self._video_service.clear_buffer()
        self._video_service.draw_actor(power)
        self._video_service.draw_actors(segments1)
        self._video_service.draw_actors(segments2)
        self._video_service.draw_actor(scores[0])
        self._video_service.draw_actor(scores[1])
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()