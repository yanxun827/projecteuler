"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""


def findPrime(position):
	primes = []
	number = 2
	while len(primes) < position:
		isprime = True
		for i in primes:
			if number%i == 0:
				isprime = False
				break
		if isprime == True:
			primes.append(number)
		number += 1
	return primes[-1]

if __name__ == "__main__":
	position = 10001
	print(findPrime(position))