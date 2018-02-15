
def isprime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number == 3:
        return True
    elif number % 2 != 0 and number % 3 != 0:
        return True
    return False


def findprimes(number):
    primesfound = ()
    counter = 2
    while len(primesfound) < number:
        if isprime(counter):
            primesfound += (counter,)
        counter += 1
    return primesfound


primesfound = findprimes(1000)
print(primesfound)