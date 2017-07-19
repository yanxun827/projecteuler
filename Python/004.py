"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def find_palindromes(btm_limit, top_limit):
	palindromes = []
	for i in range(btm_limit, top_limit):
		for j in range(btm_limit, top_limit):
			multiple = str(i * j)
			if multiple == multiple[::-1]:
				palindromes.append(int(multiple))
	return palindromes


def main():
	btm_limit = 100
	top_limit = 999
	print(max(find_palindromes(btm_limit, top_limit)))


if __name__ == '__main__':
	main()
