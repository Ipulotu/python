""" Test file for the color Class of the Dig Dug game
    Author: Ikaika Pulotu
    Comments: Jordan Greenwood
"""
import pytest
from game.shared.color import Color

def test_contractor():
    """ Testing that the contractor gets the colors according to red, green, blue, and alpha."""
    color = Color(255, 255, 255, 255)
    assert color._red == 255
    assert color._green == 255
    assert color._blue == 255 
    assert color._alpha == 255

def test__eq__():
    """ Testing the equality of the function against colors one and two"""
    color1 = Color(255, 255, 255, 255)
    color2 = Color(255, 255, 255, 255)
    assert color1 == color2
  

def test_to_tuple():
    """Testing the color to form a tuple function"""
    color1 = Color(255, 255, 255, 255)
    assert color1.to_tuple() == (255, 255, 255, 255)

pytest.main(["-v", "--tb=line", "-rN", __file__])