# derteming  if number is armstrong or not
# Luyanda Ntombela
# 18 March 2025


def is_armstrong_number(number):
    try:
        num_str = str(number)
        num_digits = len(num_str)
        total = sum(int(digit) ** num_digits for digit in num_str)
        return total == number
    except ValueError:
        return False

def main():
    user_input = input("Enter a number:\n")
    if not user_input.isdigit():
        print("Invalid input. Please enter a valid integer.")
        return
    
    number = int(user_input)
    if is_armstrong_number(number):
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")

if __name__ == "__main__":
    main()
