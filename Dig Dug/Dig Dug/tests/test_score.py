""" Testing for the Score class of Dig Dug
    Author: Kendra Anderson
    Comments: Kendra Anderson
    CSE210
"""
import pytest
from game.casting.score import Score


def test_default_class():
    """Testing for Score class to create a default score."""
    score = Score()
    assert score._points == 0
    score.add_points(0) 
    assert score._text == "Score: 0"


def test_add_points():
        """Testing for Score class to add points."""
        score = Score()
        points = 3

        score._points += points
        assert score._points == 3
        score.set_text(f"Score: {score._points}")
        assert score._text == "Score: 3"

pytest.main(["-v", "--tb=line", "-rN", __file__])