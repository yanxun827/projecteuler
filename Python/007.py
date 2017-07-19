"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""


def find_prime(position):
	primes = [2]
	number = 3
	while len(primes) != position:
		if all(number % i for i in primes) != 0:
			primes.append(number)
		number += 2
	return primes[-1]


def main():
	position = 10001
	print(find_prime(position))


if __name__ == "__main__":
	main()
