import pytest
from lib.fizzBuzz import fizzBuzz
from lib.fizzBuzz import checkFizzBuzz

# returns string 1 if number is 1

def test_returns1With1PassedIn():
    checkFizzBuzz(1, "1")

# returns string 2 if number is 2

def test_returns2With2PassedIn():
    checkFizzBuzz(2, "2")

# returns Fizz if number is 3

def test_returnsFizzWith3PassedIn():
    checkFizzBuzz(3, "Fizz")

# returns Buzzz if number is 5


def test_returnsBuzzWith5PassedIn():
    checkFizzBuzz(5, "Buzz")

# returns Fizz with multiple of 3

def test_returnsFizzWith6PassedIn():
    checkFizzBuzz(6, "Fizz")

# returns Buzz with any multiple of 5


def test_returnsBuzzWith10PassedIn():
    checkFizzBuzz(10, "Buzz")

# returns FizzBuzz if number is multiple of 3 AND 5

def test_returnsFizzBuzzWith15PassedIn():
    checkFizzBuzz(15, "FizzBuzz")
