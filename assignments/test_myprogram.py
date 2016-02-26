#!/usr/bin/env python

####################################
# in a file called test_program.py #
####################################
import myprogram
import pytest
class Test
def test_doublelit():
    assert myprogram.doubleit(10) == 20

def test_doubleit_type():
    with pytest.raises(TypeError):
        myprogram.doubleit('hello')