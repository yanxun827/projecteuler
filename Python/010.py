"""
Project Euler Problem 10
========================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def findPrime(limit):
	a = [True] * limit                          # Initialize the prime boolean list
	a[0] = a[1] = False
	for (i, isprime) in enumerate(a):
		if isprime:
			yield i
			for n in range(i*i, limit, i):     # Sieving, mark subsequent squared product as non-prime
				a[n] = False

if __name__ == '__main__':
	limit = 2000000
	print(sum(list(findPrime(limit))))