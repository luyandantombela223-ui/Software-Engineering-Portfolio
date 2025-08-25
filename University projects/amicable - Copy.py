# amicable numbers 
# Luyanda Ntombela
# 12 March 2025

def sum_of_proper_divisors(n):
    return sum(i for i in range(1, n) if n % i == 0)

def are_amicable(a, b):
    return sum_of_proper_divisors(a) == b and sum_of_proper_divisors(b) == a

a = int(input("Enter first number:\n"))
b = int(input("Enter second number:\n"))

if are_amicable(a, b):
    print(f"{a} and {b} are amicable numbers.")
else:
    print(f"{a} and {b} are not amicable numbers.")
