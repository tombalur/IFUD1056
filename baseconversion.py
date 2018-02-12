def convertfrombase10_1(number, base):
    power = 0
    result = ''
    # Finding the largest possible power
    while (number > base ** power):
        if (number < base ** (power + 1)):
            break
        power += 1
    while (power >= 0):
        divisionresult = number // base ** power
        number = number - (base ** power * divisionresult)
        result += str(divisionresult)
        power -= 1
    print(result)
    return result

def convertfrombase10_2(number, base, result=''):
    remainder = number % base
    result = str(remainder) + result
    number = number // base
    if (number == 0):
        print(result)
        return result
    else:
        convertfrombase10_2(number, base, result)

convertfrombase10_2(9, 2)
