# A program to test a function validate using statement covarage
# Luyanda Ntombela
# 24 April 2025
"""
>>> import timeutil
>>> timeutil.validate(':05 a.m.')
False
>>> timeutil.validate('622:00 p.m.')
False
>>> timeutil.validate('02:02 p.m.')
False
>>> timeutil.validate('22:14 p.t.')
False
>>> timeutil.validate('12:sd p.m.')
False
>>> timeutil.validate('12:50 a.m.')
True

"""
import doctest
doctest.testmod(verbose=True)