"""
Project Euler Problem 10
========================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def find_primes(limit):
	mask = [True] * limit  # Initialise the prime boolean
	mask[0] = mask[1] = False
	primes = []

	for num, is_prime in enumerate(mask):
		if is_prime:
			primes.append(num)
			for multiple in range(num * num, limit, num):
				# Sieving, mark subsequent multiples as non-prime. Starts with num*num instead of num*2 or num*3 etc.
				# because they would've been marked non-prime beforehand.
				mask[multiple] = False

	return primes


def main():
	limit = 2000000
	print(sum(find_primes(limit)))


if __name__ == '__main__':
	main()
