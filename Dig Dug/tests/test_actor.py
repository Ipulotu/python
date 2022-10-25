"""Test functions for the Actor Class
  Author: Ikaika Pulotu
  comments by: Jordan Greenwood
"""
import pytest
from game.casting.actor import Actor
from game.shared.color import Color
from game.shared.point import Point

def test_default_class():
  """ Test for the Actor class default functions"""
  actor = Actor()
  assert actor._text == "" 
  assert actor._font_size == 15
  assert actor._color == Color(255, 255, 255)
  assert actor._position == Point(0, 0)
  assert actor._velocity == Point(0, 0)

def test_get_color():
  """Testing that Actor class gets the color"""
  actor = Actor()
  assert Color(255, 255, 255) == actor.get_color()
  
def test_get_font_size():
  """Testing that the actor class gets the right font size"""
  actor = Actor()
  assert actor.get_font_size() == 15

def test_get_position():
  """Testing that the Actor class is able to get the right position for the player"""
  actor = Actor()
  assert actor.get_position() == Point(0, 0)
   
def test_get_text():
  """Testing for the actor class to get the text to be displayed"""
  actor = Actor()
  assert actor.get_text() == "" 
   
def test_get_velocity():
  """Testing to get the starting points and direction for the Actor"""
  actor = Actor()
  assert actor.get_velocity() == Point(0, 0)



def test_move_next():
  """Testing that the player is able to move to collect the gems."""
  actor = Actor()
  actor.set_velocity(Point(0,0))
  actor.move_next()
  x = (actor._position.get_x() + actor._velocity.get_x()) % 900
  y = (actor._position.get_y() + actor._velocity.get_y()) % 600
  assert actor._position == Point(x, y) 

def test_set_color():
  """Testing that the color aspect works for setting the color for the actor(player)"""
  actor = Actor()
  actor.set_color(Color(0, 245, 5))
  assert actor._color == Color(0, 245, 5)
    
def test_set_position():
  """Test for actors position on the playing field"""
  actor = Actor()
  actor.set_position(Point(4,6))
  assert actor._position == Point(4,6)

def test_set_font_size():
  """Testing that the font size for the actor gets set."""
  actor = Actor()
  actor.set_font_size(18)
  assert actor._font_size == 18

def test_set_text():
  """Test to see that the text gets set during gameplay"""
  actor = Actor()
  actor.set_text("text")
  assert actor._text == "text"
  

def test_set_velocity():
  """Test for movement speed"""
  actor = Actor()
  actor.set_velocity(Point(4,6))
  assert actor._velocity == Point(4,6)

pytest.main(["-v", "--tb=line", "-rN", __file__])