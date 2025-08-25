# A program to test a function format_date using path covarage
# Luyanda Ntombela
# 24 April 2025

"""
>>> import dateutil
>>> dateutil.format_date(-7,12,2023)
'Invalid date'
>>> dateutil.format_date(12,1,2023)
'12 January 2023'
>>> dateutil.format_date(32,1,2023)
'Invalid date'
>>> dateutil.format_date(12,4,2023)
'12 April 2023'
>>> dateutil.format_date(31,4,2000)
'Invalid date'
>>> dateutil.format_date(20,2,2000)
'20 February 2000'
>>> dateutil.format_date(30,2,2000)
'Invalid date'
>>> dateutil.format_date(3,2,2019)
'3 February 2019'
>>> dateutil.format_date(30,2,2019)
'Invalid date'

"""
import doctest
doctest.testmod(verbose=True)