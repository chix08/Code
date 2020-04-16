# A Better (than Naive) Solution to find all divisiors
import math


# method to print the divisors
def printDivisors(n):
    l = []
    i = 1
    while i <= math.sqrt(n):
        if (n % i == 0):
            if (n / i == i):
                l.append(i)
            else:
                l.append(i)
                l.append(n // i)
        i = i + 1

    return l


# Driver method


# Python 3 program to find count of
# primes in given array.
from math import sqrt

max_val = 1000001
prime = [True for i in range(max_val + 1)]


def sev():
    # Remaining part of SIEVE
    prime[0] = False
    prime[1] = False
    k = int(sqrt(max_val)) + 1
    for p in range(2, k, 1):

        # If prime[p] is not changed,
        # then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * 2, max_val + 1, p):
                prime[i] = False


# Function to find count of prime
def primeCount(arr, n):
    # Find maximum value in the array

    # Find all primes in arr[]
    count = 0
    for i in range(0, n, 1):
        if (prime[arr[i]]):
            count += 1

    return count


# This code is contributed by
# Shashank_Sharma
sev()
t = {}
for i in range(200000,300000):
    z = printDivisors(i)
    if primeCount(z, len(z)) == 1:
        print()
        t[len(z)]=t.get(len(z),0)+1

    if i%50000 == 0:
        print()

# print(t)
# This code is contributed by Nikita Tiwari.
print()

#[4, 6, 8, 9, 10, 12, 15, 14, 16, 18, 20, 21, 24, 25, 28, 27, 30, 22, 32, 35, 36, 33, 40, 26, 42, 45, 44, 48, 39, 50, 49, 54, 55, 56, 52, 60, 63, 34, 66, 64]