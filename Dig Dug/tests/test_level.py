""" Testing for the level class of Dig Dug
    Author: Kendra Anderson
    Comments: Jordan Greenwood
    CSE210
"""
import pytest
import constants
from game.casting.level import Level


def test_add_dirt():
    """Testing for the dirt function adding dirt."""

    level = Level()
    level.add_dirt()
    assert level.levelCast.get_first_actor('dirt')._text == "#"
    assert level.levelCast.get_first_actor('dirt')._color == constants.BROWN


def test_add_grass():
    """Testing for the grass function adding grass."""

    level = Level()
    level.add_grass()
    assert level.levelCast.get_first_actor('grass')._text == "%"
    assert level.levelCast.get_first_actor('grass')._color == constants.GREEN


def test_add_stones():
    """Testing for the stone function adding stones."""

    level = Level()
    level.add_stones()
    assert level.levelCast.get_first_actor('stones')._text == "O"
    assert level.levelCast.get_first_actor('stones')._color == constants.gray
 

def test_add_gems():
    """Testing for the gems function adding gems."""

    level = Level()
    level.add_gems()
    assert level.levelCast.get_first_actor('gems')._text =="*"


pytest.main(["-v", "--tb=line", "-rN", __file__])