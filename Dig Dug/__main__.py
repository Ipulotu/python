"""The Main file that starts the game running through the functions.
   Author: Ikaika Pulotu
   Comments by: Jordan Greenwood
"""
import constants
from game.casting.actor import Actor
from game.casting.level import Level
from game.casting.cast import Cast
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.point import Point


def main():
    """The main function that starts up all the differing
    functions within the game."""
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner_score = Actor()
    banner_score.set_text("Score: 0")
    banner_score.set_font_size(constants.FONT_SIZE)
    banner_score.set_color(constants.WHITE)
    banner_score.set_position(Point(constants.CELL_SIZE, 0))
    cast.add_actor("banners", banner_score)

    banner_lives = Actor()
    banner_lives.set_text("Lives: Q Q Q")
    banner_lives.set_font_size(constants.FONT_SIZE)
    banner_lives.set_color(constants.WHITE)
    banner_lives.set_position(Point(constants.CELL_SIZE+100, 0))
    cast.add_actor("banners", banner_lives)
    
    banner_gameover = Actor()
    banner_gameover.set_text("")
    banner_gameover.set_font_size(constants.FONT_SIZE*2)
    banner_gameover.set_color(constants.WHITE)
    banner_gameover.set_position(Point(round(constants.MAX_X/2), round(constants.MAX_Y/2)))
    cast.add_actor("banners", banner_gameover)
    
    
    # create the robot
    player = Actor()
    player.set_text("@")
    player.set_font_size(constants.FONT_SIZE)
    player.set_color(constants.WHITE)
    player.set_position(constants.START_POSITION)
    cast.add_actor("players", player)


    level = Level()
    cast.add_group(level.levelCast, 'dirt')
    cast.add_group(level.levelCast, 'grass')
    cast.add_group(level.levelCast, 'gems')
    cast.add_group(level.levelCast, 'stones')
    
    
    # start the game
    keyboard_service = KeyboardService(constants.CELL_SIZE)
    video_service = VideoService(constants.CAPTION, constants.MAX_X, constants.MAX_Y, constants.CELL_SIZE, constants.FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)

if __name__ == "__main__":
    main()