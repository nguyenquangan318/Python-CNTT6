import pytest

def divide(first, second):
    if(second == 0):
        return
    result = first / second
    return result

def test_happy_case():
    assert divide(10, 5) == 2
    
def test_divide_by_zero():
    assert divide(10, 0) == None