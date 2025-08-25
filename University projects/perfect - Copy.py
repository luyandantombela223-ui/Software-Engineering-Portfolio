# program to determine if a number is a perfect number or not.
# Luyanda Ntombela 
# 10 March 2024



def perfect_number(n):
    divisors = [] 
    sum_of_divisors = 0 

    for i in range(1, n):
        if n % i == 0:
            divisors.append(i) 
            sum_of_divisors += i 

    print("The proper divisors of", n, "are:")
    print(*divisors, sep=' ')
    print()

    if sum_of_divisors == n:
        print(f"{n} is a perfect number.")
    else:
        print(f"{n} is not a perfect number.")

perfect_number(int(input("Enter a number:\n")))

