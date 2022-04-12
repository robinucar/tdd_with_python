def fizzBuzz(num):
    if isMultiple(num, 3):
        if isMultiple(num, 5):
            return 'FizzBuzz'
        return 'Fizz'
    if isMultiple(num, 5):
        return 'Buzz'
    return str(num)


def isMultiple(value, mod):
    return (value % mod) == 0


def checkFizzBuzz(value, expectedRetVal):
    retVal = fizzBuzz(value)
    assert retVal == expectedRetVal
