""" Testing for the Collision class of Dig Dug
    Author: Kendra Anderson
    Comments: Jordan Greenwood
    CSE210
"""
import pytest
from game.directing.handle_collision import Handle_collision
from game.casting.cast import Cast

def test_default_class():
    """ Testing the the game functions work with regards
    to the collisions of the actor and the set pieces."""
    collision = Handle_collision()

    assert collision.lives == 3
    assert collision.score == 0
    assert collision._is_game_over == False


def test_execute():
    """Making sure that the collision function executes."""
    collision = Handle_collision()
    cast = Cast()
    collision.execute(cast)
    
    assert collision._is_game_over == False


def test_handle_gem_collision():
    """ Checks for how the game handles gem collisions."""
    collision = Handle_collision()
    cast = Cast()
    assert collision.handle_gem_collision(cast)

def test_cast_get_actors(self, cast):
    """Testing for the collison with the players piece and what happens
    when they collide with a gem or a rock."""
    for i in cast.get_actors("gems"):
        if self.player.get_position().equals(i.get_position()):
            assert self.socore == 100
            assert self.banner_score.set_text(f"Score: {self.socore}")
            assert cast.remove_actor("gems", i)
        if self.lives < 0:
            assert cast.remove_actor("gems", i)


def test_handle_grass_collision(self, cast):
    """Testing for what happens to the grass when the player
    collides with it."""
    for i in cast.get_actors("grass"):
        if self.player.get_position().equals(i.get_position()):
            assert cast.remove_actor("grass", i)
        if self.lives < 0:
            assert cast.remove_actor("grass", i)


def test_handle_dirt_collision(self, cast):
    """Testing for what happens with the dirt when the player collides with it."""
    for i in cast.get_actors("dirt"):
        if self.player.get_position().equals(i.get_position()):
            assert cast.remove_actor("dirt", i)
        if self.lives < 0:
            assert cast.remove_actor("dirt", i)

def test_handle_enemy_collision(self, cast, constants):
    """ Testing for enemy collision in the game with the player."""
    for i in cast.get_actors("enemy"):
        if self.player.get_position().equals(i.get_position()):
            assert self.lives == 1
            assert self.player.set_position(constants.START_POSITION)
            assert cast.remove_actor("enemy", i)
        if self.lives < 0:
            assert cast.remove_actor("enemy", i)


def test_handle_stone_collision(self, cast, constants):
    """Testing for how the stones interact with the player."""
    for i in cast.get_actors("stones"):

        if self.player.get_position().equals(i.get_position()):
            assert self.lives == 1
            assert self.player.set_position(constants.START_POSITION)
            if self.lives == 2:
                assert self.banner_lives.set_text(f"Lives Q Q")
            elif self.lives == 1:
                assert self.banner_lives.set_text(f"Lives Q ")
            elif self.lives == 0:
                assert self.banner_lives.set_text(f"Lives  ")
        if self.lives < 0:
            assert cast.remove_actor("stones", i)


def test_handle_game_over(self, cast):
    """Testing for how the game handles game over message."""
    if self.lives < 0:
        banner_gameover = cast.get_actors("banners")[2]
        assert banner_gameover.set_text("Game Over")


pytest.main(["-v", "--tb=line", "-rN", __file__])
