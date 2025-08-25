# using newton for approximation
# Luyanda Ntombela
# 14 March 2025
import math

import math

def newton_ln(s, precision):
    x_prev = s
    while True:
        x_next = x_prev - ((math.exp(x_prev) - 1 - s) / math.exp(x_prev))
        if abs(x_next - x_prev) <= precision:
            return round(x_next, 4)
        x_prev = x_next

def main():
    s = float(input("Enter a value for S: "))
    precision = float(input("Enter a value for the required precision: "))
    approximation = newton_ln(s, precision)
    print(f"The approximation is {approximation}.")

if __name__ == "__main__":
    main()


