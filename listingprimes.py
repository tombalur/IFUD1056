#!/usr/bin/python3
# File name: listingprimes.py
# Author: Tom Are Tørum
# Submission: Assignment 3
# Source: https://www.youtube.com/watch?v=klcIklsWzrY
# Using Sieve of Eratosthenes method to find primes from 2 to n


def printprimes(number):
    ''' Find primes 2 to n.
    :param int number: List primes from 2 to number
    :return None
    '''
    # Checking if number is int and larger than 1
    if type(number) != int or number < 2:
        print("Number must be integer and larger than 1")
        return None
    # Creating a boolean list of n elements
    primes = [True] * number
    # counter for looping through the list
    p = 2
    # Run while p squared is smaller or equal to number
    while p ** 2 <= number:
        # Checking if number is already set to false
        if primes[p]:
            # Set all multiplications of p to false
            for i in range(p * 2, number, p):
                primes[i] = False
        p += 1
    # Print prime numbers
    for i in range(2, number):
        if primes[i]:
            print(i)
    return None


printprimes(number=1000)
