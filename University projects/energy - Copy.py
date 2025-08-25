# Calculating the energy
# Luyanda Ntombela
# 28 February 2025

numbers = input("Enter numbers separated by spaces: ")
numbers = list(map(int,numbers.split()))
d = []  # Initialize the list outside the loop

for i in numbers:
    if i % 2 == 0:
        d.append(i)  # Append even numbers to the list
print(d)





