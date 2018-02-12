import time


def convertfrombase10_1(number, base):
    power = 0
    result = ''
    # Finding the largest possible power
    while number > base ** power:
        if number < base ** (power + 1):
            break
        power += 1
    # Floor dividing the number with the highest posible power. Subtracting the ...
    while power >= 0:
        divisionresult = number // base ** power
        number = number - (base ** power * divisionresult)
        result += str(divisionresult)
        power -= 1
    return int(result)


def convertfrombase10_2(number, base, result=''):
    remainder = number % base
    result = str(remainder) + result
    number = number // base
    if number == 0:
        return int(result)
    else:
        return convertfrombase10_2(number, base, result)


def converttobase10(number, base):
    numbersplit = tuple(str(number))
    i = len(numbersplit) - 1
    result = 0
    for digit in numbersplit:
        result = result + (base ** i * int(digit))
        i -= 1
    return result


base = 5
number = 1455654
starttime = time.time()
result = convertfrombase10_1(number, base)
endtime = time.time()
print('Solution 1, convert from base10:')
print('Convert base10 number ' + str(number) + ' to base' + str(base) + ' result: ' + str(result))
print('Execution time ' + str((endtime-starttime) * 1000) + ' ms.\n')
starttime = time.time()
result = convertfrombase10_2(number, base)
endtime = time.time()
print('Solution 2, convert from base10:')
print('Convert base10 number ' + str(number) + ' to base' + str(base) + ' result: ' + str(result))
print('Execution time ' + str((endtime-starttime) * 1000) + ' ms.\n')
starttime = time.time()
number = 333040104
result = converttobase10(number, base)
endtime = time.time()
print('Solution 3, convert to base10:')
print('Convert base' + str(base) + ' number ' + str(number) + ' to base10 result: ' + str(result))
print('Execution time ' + str((endtime-starttime) * 1000) + ' ms.')

