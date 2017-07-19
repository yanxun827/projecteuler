"""
Project Euler Problem 6
=======================

The sum of the squares of the first ten natural numbers is,
                       1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
                    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""


def squared_diff_sum(number):
	sum_squared = sum([i for i in range(number + 1)]) ** 2
	squared_sum = sum([i ** 2 for i in range(number + 1)])
	return sum_squared - squared_sum


def main():
	number = 100
	print(squared_diff_sum(number))


if __name__ == '__main__':
	main()
