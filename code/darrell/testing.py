import pytest

def go_hiking(energy, weather):
    if energy == "tired" and weather == "rainy":
        return False
    elif energy == "tired" and weather == "sunny":
        return False
    elif energy == "spry" and weather == "rainy":
        return False
    elif energy == "spry" and weather == "sunny":
        return True

def test_go_hiking():
    assert go_hiking('tired', 'rainy') == False
    assert go_hiking('tired', 'sunny') == False
    assert go_hiking('spry', 'rainy') == False
    assert go_hiking('spry', 'sunny') == True