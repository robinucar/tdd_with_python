def fizzBuzz(num):
    if num == 3:
        return 'Fizz'
    if num == 5:
        return 'Buzz'
    return str(num)

def checkFizzBuzz(value, expectedRetVal):
    retVal = fizzBuzz(value)
    assert retVal == expectedRetVal