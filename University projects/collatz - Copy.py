# collatz sequence array
# Luyanda Ntombela
# 18 March 2025

def collatz_sequence(number):
    sequence = []
    while number != 1:
        sequence.append(number)
        if number % 2 == 0:  # If the number is even
            number = number // 2
        else:  # If the number is odd
            number = 3 * number + 1
    sequence.append(1)  # Add the final 1 to the sequence
    return sequence

def main():
    user_input = input("Enter a positive integer:\n")
    
    # Validate the input
    try:
        number = int(user_input)
        if number <= 0:
            print("Please enter a positive integer.")
        else:
            sequence = collatz_sequence(number)
            print(" ".join(map(str, sequence)))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
