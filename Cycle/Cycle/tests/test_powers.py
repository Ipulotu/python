""" Testing for the Powers class of Cycle
    Author: Kendra Anderson
    Comments: Kendra Anderson
    CSE210
"""
import pytest
from game.casting.powers import Powers
from game.shared.point import Point
import random
import constants


def test_default_class():
    """Testing that the class creates the Powers."""
    powers = Powers()
    powers.set_text("@")
    assert powers._text == "@"
    powers.set_color(constants.YELLOW)
    assert powers._color == constants.YELLOW
 
def test_reset():
    """Tests for the reset method to reset all its attributes."""

    powers = Powers()

    powers._points = random.randint(1, 8)
    assert powers._points > 0 and powers._points < 9
    x = random.randint(1, constants.COLUMNS - 1)
    assert x > 0 and x < 39
    y = random.randint(1, constants.ROWS - 1)
    assert y > 0 and y < 19
    position = Point(x, y)
    assert position._x == x
    assert position._y == y
    position = position.scale(constants.CELL_SIZE)
    powers.set_position(position)


pytest.main(["-v", "--tb=line", "-rN", __file__])