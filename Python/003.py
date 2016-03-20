"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

def largest_prime_factors(n):
	i = 2
	factors = []
	while i * i <= n:
		if n % i: # True means there is a remainder
			i += 1
		else:
			n //= i
			factors.append(i)
	if n > 1:
		factors.append(n)
	return factors[-1] # Largest prime at the end of list

if __name__ == '__main__':
	number = 600851475143
	print(largest_prime_factors(number))