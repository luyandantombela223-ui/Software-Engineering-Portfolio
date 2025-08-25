# A program to test a function roman using path covarage
# Luyanda Ntombela
# 24 April 2025

"""
>>> import romanutil
>>> romanutil.from_roman('IX')
9
>>> romanutil.from_roman('XI')
11
>>> romanutil.from_roman('X')
10
>>> romanutil.from_roman('')
0
>>> romanutil.from_roman('III')
3
>>> romanutil.from_roman('XIV')
14

"""

import doctest
doctest.testmod(verbose=True)