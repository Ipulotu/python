""" Testing for the Cycle class of Cycle
    Author: Kendra Anderson
    Comments: Kendra Anderson
    CSE210
"""
import constants
import pytest
from game.casting.cycle import Cycle
from game.shared.point import Point
from game.casting.actor import Actor
from game.shared.color import Color
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.script import Script

hca = HandleCollisionsAction()
script = Script()
control = ControlActorsAction(script, hca)
start = 3
color = constants.CYAN

def test_default_class():
    """ Test for the default functions for the Cycle class."""
    cycle = Cycle(constants.CYAN, 3)
    assert len(cycle._segments) == 2  
    assert cycle._color == constants.CYAN


def test_get_segments():
    """Testing for the Cycle class to get the tail."""
    cycle = Cycle(constants.CYAN, 3)
    assert len(cycle.get_segments()) == 2
   


def test_set_color():
    """Testing for the Cycle class to set the color."""
    cycle = Cycle(constants.CYAN, 3)
    cycle.set_color(Color(5, 5, 255))
    assert cycle._color == Color(5, 5, 255)


def test_get_head():
    """Testing for the Cycle class to get the head segment."""
    cycle = Cycle(constants.CYAN, 3)
    assert cycle._segments[0]._text == "@"


def test_grow_tail():
    """Testing for Cycle class to grow the tail."""
    cycle = Cycle(constants.CYAN, 3)
    cycle.grow_tail(1)
    assert len(cycle._segments) == 3


def test_prepare_body():
    """Testing for Snake class to prepare the body."""
    cycle = Cycle(constants.CYAN, 3)
    cycle._prepare_body(3)
   
    assert cycle._segments[0]._text == "@"
    assert cycle._segments[1]._text == "u'\U0001F427'"


pytest.main(["-v", "--tb=line", "-rN", __file__])
