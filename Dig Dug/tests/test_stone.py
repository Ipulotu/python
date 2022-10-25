""" Testing for the Cycle class of Cycle
    Author: Kendra Anderson
    Comments: Jordan Greenwood
    CSE210
"""
import pytest
import constants
from game.casting.stone import Stone
from game.casting.level import Level


def test_place_stone():
    """Testing for the placement of the stones."""
    stone = Stone()
    level = Level()
    stone.place_stone(level.levelCast)
    assert stone._text == "O"
    assert stone._color == constants.gray


pytest.main(["-v", "--tb=line", "-rN", __file__])