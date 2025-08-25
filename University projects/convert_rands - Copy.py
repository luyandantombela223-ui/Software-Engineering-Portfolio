# A program that converts an amount of money (in cents) into equivalent dollars, 
# quarters, dimes, nickels, and pennies
#
# Lebeko Poulo
#
# 20 February 2025
#
cents = int(input("Enter the amount in cents: "))
rands = cents // 100
cents = cents % 100

fifty_cents = cents // 50
cents = cents % 50
twenty_cents = cents // 20
cents = cents % 20
ten_cents = cents // 10
cents = cents % 10
five_cents = cents // 5
cents = cents % 5
one_cents = cents
print(f"{rands} Rands, {fifty_cents} x 50c, {twenty_cents} x 20c, {ten_cents} x 10c, {five_cents} x 5c, {one_cents} x 1c")
