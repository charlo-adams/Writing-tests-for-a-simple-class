from lib.highValue import *

def test_get_highest():
    our_values = HighValue(33, 90)
    assert our_values.get_highest() == "Second value is higher"


def test_negative_numbers():

def test_get_first_highest():
    our_values = HighValue(88, 12)
    assert our_values.get_highest() == "First value is higher"

def test_values():
    values = HighValue(50, 50)
    assert values.get_highest() == "Values are equal"

def test_add():
    our_values = HighValue(68, 40)
    our_values.add(15, "first")
    assert our_values.value_first == 83

def test_add_again():
    our_values = HighValue(68, 40)
    our_values.add(15, "second")
    assert our_values.value_second == 55