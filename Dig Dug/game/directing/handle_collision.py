"""Collision handling class for the Dig Dug game.
   Author: Ikaika Pulotu
   Comments: Jordan Greenwood
   Edits by: Kendra Anderson
"""
import constants


class Handle_collision:

    def __init__(self, cast):
        """Constructor function to start the instances 
           surrounding the collisions in gameplay
        """
        self.player =  cast.get_first_actor("players")
        self.lives = 3
        self.score = 0
        self._is_game_over = False
        self.banner_score = cast.get_first_actor("banners")
        self.banner_lives = cast.get_actors("banners")[1]

    def execute(self, cast):
        """Executes the handle collisions action.
        Args:
            cast (Cast): The cast of Actors in the game.

        """
        if not self._is_game_over:
            self._handle_gem_collision(cast)
            self._handle_grass_collision(cast)
            self._handle_dirt_collision(cast)
            self._handle_enemy_collision(cast)
            self._handle_stone_collision(cast)
            self._handle_game_over(cast)

    def _handle_gem_collision(self, cast):
        """Function for the handling of the gems colliding with player.
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        for i in cast.get_actors("gems"):
            if self.player.get_position().equals(i.get_position()):
                self.score += 100
                self.banner_score.set_text(f"Score: {self.score}")
                cast.remove_actor("gems", i)
            if self.lives < 0:
                cast.remove_actor("gems", i)

    def _handle_grass_collision(self, cast):
        """Function for the handling of the grass colliding with player.
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        for i in cast.get_actors("grass"):
            if self.player.get_position().equals(i.get_position()):
                cast.remove_actor("grass", i)
            if self.lives < 0:
                cast.remove_actor("grass", i)

    def _handle_dirt_collision(self, cast):
        """Function for the handling of the grass colliding with player.
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        for i in cast.get_actors("dirt"):
            if self.player.get_position().equals(i.get_position()):
                cast.remove_actor("dirt", i)
            if self.lives < 0:
                cast.remove_actor("dirt", i)

    def _handle_enemy_collision(self, cast):
        """Function for the handling of the enemies colliding with player.
        Args:
            cast (Cast): The cast of Actors in the game.
        """                     ## ------------------------- Needs work----------------------------------
        for i in cast.get_actors("enemy"):
            if self.player.get_position().equals(i.get_position()):
                self.lives -= 1
                self.player.set_position(constants.START_POSITION)
                cast.remove_actor("enemy", i)
            if self.lives < 0:
                cast.remove_actor("enemy", i)

    def _handle_stone_collision(self, cast): 
        """Function for the handling of the stones colliding with player.
        Args:
            cast (Cast): The cast of Actors in the game.
        """       
        for i in cast.get_actors("stones"):
            
            if self.player.get_position().equals(i.get_position()):
                self.lives -= 1
                self.player.set_position(constants.START_POSITION)
        
        if self.lives == 2:
            self.banner_lives.set_text(f"Lives Q Q")
        elif self.lives == 1:
            self.banner_lives.set_text(f"Lives Q ")
        elif self.lives == 0:
            self.banner_lives.set_text(f"Lives  ")
        if self.lives < 0:
            cast.remove_actor("stones", i)

    def _handle_game_over(self, cast):
        """Function for the handling of the game when the player is out of lives.
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self.lives < 0:
           banner_gameover = cast.get_actors("banners")[2]
           banner_gameover.set_text("Game Over")

            


            

