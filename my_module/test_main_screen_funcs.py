"""Test for my functions."""

from main_screen_funcs import *

def test_rand_x_offset():
    temp = rand_x_offset()
    assert (temp in range(0, 144)) or (temp in range (-144, 0))
    assert temp % 24 == 0

def test_rand_y_offset():
    temp = rand_y_offset()
    assert temp in range (48, 144)
    assert temp % 24 == 0

def test_correct_x_pos():
    temp0 = [500, 500]
    correct_x_pos(temp0)
    assert temp0[1] == 500
    assert temp0[0] in range(336, 409)
    assert temp0[0] % 24 == 0

    temp1 = [-10, 300]
    correct_x_pos(temp1)
    assert temp1[1] == 300
    assert temp1[0] in range(0, 72)
    assert temp1[0] % 24 == 0
