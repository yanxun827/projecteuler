"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""


def smallest_common_multiple(limit):
	num = 1
	i = 1
	while i <= limit:
		if num%i == 0: # check if num can be evenly divided by i
			i += 1
			step = num
		else:
			num += step # look for smallest number divisible by i,
						# by incrementing at number divisible by from 1 to i-1
	return num

if __name__ == '__main__':
	limit = 20
	print(smallest_common_multiple(limit))

