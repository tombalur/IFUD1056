def isprime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    counter = 5
    while counter ** 2 <= number:
        if number % counter == 0 or number % (counter + 2) == 0:
            return False
        counter += 1
    return True


def isprimefermat(number):
    randomnumber = 5
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    elif randomnumber ** number % number == 1:
        return True
    return False


def findprimes(number):
    primesfound = ()
    counter = 0
    while len(primesfound) < number:
        if isprimefermat(counter):
            primesfound += (counter,)
        counter += 1
    return primesfound


#primesfound = findprimes(5)
#print(primesfound)