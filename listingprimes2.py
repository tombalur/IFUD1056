#!/usr/bin/python3
# File name: listingprimes2.py
# Author: Tom Are Tørum
# Submission: Assignment 3
# https://en.wikipedia.org/wiki/Primality_test
import time

def isprime(number):
    '''Primality test
    :param int number: Number to be tested
    :return bool
    '''
    if number < 2:
        return False
    if number <= 3:
        return True
    if number % 2 == 0:
        return False
    i = 3
    while i * i <= number:
        if number % i == 0:
            return False
        i = i + 2
    return True


def findprimes(amount):
    '''Find n amount of primes
    :param int amount: The amount of primes you want returned
    :return None:
    '''
    primesfound = ()
    counter = 0
    prime = 0
    while prime < amount:
        if isprime(counter):
            print(counter)
            prime += 1
        counter += 1
    return None


primesfound = findprimes(amount=1000)
