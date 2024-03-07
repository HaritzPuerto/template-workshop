import pytest
from template_workshop import Fibonacci


def test_import():
    # This checks __init__ was set up correctly
    try:
        from template_workshop import Fibonacci
    except ImportError:
        assert False


##### YOUR CODE HERE #####
def test_fibonnaci():
    fib = Fibonacci()
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(-1) == None
    assert fib.fib(10) == 55


def test_fibonnaci_memoization():
    fib = Fibonacci()
    assert fib(10) == 55


##########################
