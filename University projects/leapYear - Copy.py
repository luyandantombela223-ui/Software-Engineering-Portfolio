# dertiming if year is a leap year or not 
# Luyanda Ntombela
# 03 March 2025

year = int(input("Enter a year:\n"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leap year.")
        else:
            print(year, "is not a leap year.")
    else:
        print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")




