import pytest
from lib.fizzBuzz import fizzBuzz

def test_returns1With1PassedIn():
    retVal = fizzBuzz(1)
    assert retVal == '1'

def test_returns2With2PassedIn():
    retVal = fizzBuzz(2)
    assert retVal == "2"