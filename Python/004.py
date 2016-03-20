"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def largestPalindrome(toplimit, btmlimit):
	palindromes = []

	for i in range(toplimit, btmlimit, -1):
		for j in range(toplimit, btmlimit, -1):
			num = i*j
			if str(num) == str(num)[::-1]:
				btmlimit = j
				palindromes.append(num)

	return max(palindromes)


if __name__ == '__main__':
	toplimit = 999
	btmlimit = 100
	print(largestPalindrome(toplimit, btmlimit))