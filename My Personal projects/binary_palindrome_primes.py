# A code to find binary prime palindrome numbers
# Luyanda Ntombela
# 01 May 2025

import sys
sys.setrecursionlimit(30000)

def is_prime(n, divisor=2):
    # Check if num is prime using recursion
    if n < 2:
        return False
    if divisor**2 > n:
        return True
    if n % divisor == 0:
        return False
    else:
        return is_prime(n, divisor + 1)

def to_binary(n):
    # Convert number to binary recursively
    if n == 0:
        return ''
    else:
        return to_binary(n // 2) + str(n % 2)

def is_palindrome(s, left=0):
    # Check if string is palindrome recursively
    if left >= len(s) // 2:
        return True
    if s[left] != s[len(s) - left - 1]:
        return False
    else:
        return is_palindrome(s, left + 1)

def find_palindrome_primes(current, end):
    # Go through each number and check conditions
    if current > end:
        return
    binary_str = to_binary(current)
    if is_prime(current) and is_palindrome(binary_str):
        print(str(current) + " (binary: " + binary_str + ")")
    find_palindrome_primes(current + 1, end)

def main():
    # Get user input
    m = int(input("Enter the starting point M:\n"))
    n = int(input("Enter the ending point N:\n"))
    print("Binary palindrome primes between " + str(m) + " and " + str(n) + " are:")
    find_palindrome_primes(m, n)

if __name__ == "__main__":
    main()
