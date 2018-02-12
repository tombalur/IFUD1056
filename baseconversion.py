#!/usr/bin/python3
# File name: baseconversion.py
# Author: Tom Are Tørum
# Submission: Assignment 2
import time


def convertfrombase10_1(number, base):
    '''Convert from base10
    :param int number: Number to be converted
    :param int base: Type of base
    :return int result: Number in new base
    '''
    power = 0
    result = ''
    # Finding the largest possible power
    while number > base ** power:
        if number < base ** (power + 1):
            break
        power += 1
    # Looping through power, calculating result
    while power >= 0:
        divisionresult = number // base ** power
        number = number - (base ** power * divisionresult)
        result += str(divisionresult)
        power -= 1
    return int(result)


def convertfrombase10_2(number, base, result=''):
    '''Convert from base10
    :param int number: Number to be converted
    :param int base: Type of base
    :return int result: Number in new base
    '''
    # Calculating result
    remainder = number % base
    result = str(remainder) + result
    number = number // base
    # If floor division reaches 0 return value, else continue recursion
    if number == 0:
        return int(result)
    else:
        return convertfrombase10_2(number, base, result)


def converttobase10(number, base):
    '''Convert to base10
    :param int number: Number to be converted
    :param int base: Type of base
    :return int result: Number in new base
    '''
    # Converting number to string and splitting it into tuple
    numbersplit = tuple(str(number))
    # Finding length of tuple
    i = len(numbersplit) - 1
    result = 0
    # Looping through tuple, calculating result
    for digit in numbersplit:
        result = result + (base ** i * int(digit))
        i -= 1
    return result


# Calculating solution 1
base = 5
number = 223
starttime = time.time()
result = convertfrombase10_1(number, base)
endtime = time.time()
print('Solution 1, convert from base10:')
print('Convert base10 number ' + str(number) + ' to base' + str(base) + ' result: ' + str(result))
print('Execution time ' + str((endtime-starttime) * 1000) + ' ms.\n')

# Calculating solution 2
starttime = time.time()
result = convertfrombase10_2(number, base)
endtime = time.time()
print('Solution 2, convert from base10:')
print('Convert base10 number ' + str(number) + ' to base' + str(base) + ' result: ' + str(result))
print('Execution time ' + str((endtime-starttime) * 1000) + ' ms.\n')

# Calculating solution 3
starttime = time.time()
number = 1343
result = converttobase10(number, base)
endtime = time.time()
print('Solution 3, convert to base10:')
print('Convert base' + str(base) + ' number ' + str(number) + ' to base10 result: ' + str(result))
print('Execution time ' + str((endtime-starttime) * 1000) + ' ms.')
