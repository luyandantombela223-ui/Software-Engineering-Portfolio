# A program to test a function palindrome using statement covarage
# Luyanda Ntombela
# 24 April 2025
"""
>>> import palindrome
>>> palindrome.is_palindrome('')
True
>>> palindrome.is_palindrome('F')
True
>>> palindrome.is_palindrome('abccxa')
False
>>> palindrome.is_palindrome('TRUE')
False
>>> palindrome.is_palindrome('level')
True

"""
import doctest
doctest.testmod(verbose=True)
