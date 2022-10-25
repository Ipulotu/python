""" Testing for the Cast class of Cycle
    Author: Ikaika Pulotu
    Comments: Jordan Greenwood
    CSE210
"""
import pytest
from game.casting.cast import Cast
from game.casting.actor import Actor


def test_defalt_class():
    """ Testing that the class casts the actors."""
    cast = Cast()
    assert cast._actors == {}
    
        
def test_add_actor():
    """ Testing the add_actor function to ensure it correctly adds an actor"""
    actor = Actor()
    cast = Cast()
    cast.add_actor("group1", actor) 
    assert cast.get_all_actors() == [actor]


def test_get_actors():
    """ Testing the function to get more actors for the game."""
    actor1 = Actor()
    actor2 = Actor()
    cast = Cast()
    cast.add_actor("group1", actor1) 
    cast.add_actor("group1", actor2) 
    print(cast.get_actors("group1"))
    assert cast.get_actors("group1") == [actor1, actor2]
 

def test_get_all_actors():
    """ Testing the function to get all actors and group them together"""
    actor1 = Actor()
    actor2 = Actor()
    cast = Cast()
    cast.add_actor("group1", actor1) 
    cast.add_actor("group2", actor2)
    assert cast.get_all_actors() == [actor1, actor2]
      

def test_get_first_actor():
    """ Test function for getting a specific actor from the group"""
    actor1 = Actor()
    actor2 = Actor()
    cast = Cast()
    cast.add_actor("group1", actor1) 
    cast.add_actor("group1", actor2)
    assert cast.get_first_actor("group1")  == actor1
    

def test_remove_actor():
    """ Test function for removing an actor from the group."""
    actor1 = Actor()
    cast = Cast()
    cast.add_actor("group1", actor1) 
    cast.remove_actor("group1", actor1)  
    assert cast.get_all_actors() == []

pytest.main(["-v", "--tb=line", "-rN", __file__])