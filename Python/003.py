"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""


def largest_prime_factor(number):
	i = 2
	prime_factors = []
	while i <= number:
		if number % i == 0:  # Is prime factor.
			prime_factors.append(i)
			number = number / i
		else:
			i += 1
	return prime_factors[-1]


def main():
	number = 600851475143
	print(largest_prime_factor(number))


if __name__ == '__main__':
	main()
