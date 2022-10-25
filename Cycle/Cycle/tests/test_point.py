""" Test file for the Point class of the Cycle game
    Author: Ikaika Pulotu
    Comments: Jordan Greenwood
"""
import pytest
from game.shared.point import Point

def test_contractor():
    """ Testing the contractor function to get the points for the game play"""
    point = Point(0,1)
    assert point._x == 0
    assert point._y == 1

def test_add():
    """ Testing the add function of the points"""
    point1 = Point(0,1)
    point2 = Point(0,1)
    point1.add(point2)
    assert point1._y == 1


def test_get_x():
    """ Testing the functions ability to get the point for 'x' """
    point = Point(0,1)
    assert point.get_x() == 0

def test_get_y():
    """ Testing the functions ability to get the point for 'y' """
    point = Point(0,1)
    assert point.get_y() == 1

@pytest.mark.parametrize("p1, p2, factor",
 [(1, 1, 1),
  (4, 2, 6),
  (12, 7, 0),
 ])
 
def test_scale(p1, p2, factor):
    """ Test the scale of the point factoring."""
    point = Point(p1, p2)
    assert point.scale(factor) == Point(p1*factor, p2*factor)
    
pytest.main(["-v", "--tb=line", "-rN", __file__])