"""
Project Euler Problem 2
=======================

Each new term in the Fibonacci sequence is generated by adding the
previous two terms. By starting with 1 and 2, the first 10 terms will be:

                  1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Find the sum of all the even-valued terms in the sequence which do not
exceed four million.
"""


def sum_even_fibonacci(limit):
	total = 0
	number, next_num = 1, 2
	while number < limit:
		if number % 2 == 0:
			total += number
		number, next_num = next_num, number + next_num
	return total


def main():
	limit = 4000000
	print(sum_even_fibonacci(limit))


if __name__ == '__main__':
	main()
