def fizzBuzz(num):
    if num == 3:
        return 'Fizz'
    return str(num)

def checkFizzBuzz(value, expectedRetVal):
    retVal = fizzBuzz(value)
    assert retVal == expectedRetVal