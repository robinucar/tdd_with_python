import pytest
from lib.fizzBuzz import fizzBuzz

def test_returns1With1PassedIn():
    retVal = fizzBuzz(1)
    assert retVal == '1'