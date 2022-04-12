import pytest
from lib.fizzBuzz import fizzBuzz
from lib.fizzBuzz import checkFizzBuzz

def test_returns1With1PassedIn():
    checkFizzBuzz(1, "1")

def test_returns2With2PassedIn():
    checkFizzBuzz(2, "2")

def test_returnsfizzWith3PassedIn():
    checkFizzBuzz(2, "Fizz")