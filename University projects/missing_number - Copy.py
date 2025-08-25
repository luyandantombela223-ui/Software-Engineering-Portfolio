# Finding the missing number if it is present
# Luyanda Ntombela
# 22 March 2025 

# missing_number.py

def find_missing_number(numbers):
    # Find the smallest and largest numbers in the range
    min_num, max_num = min(numbers), max(numbers)
    
    # Calculate the expected sum of the full range of numbers
    expected_sum = sum(range(min_num, max_num + 1))
    
    # Calculate the actual sum of the given numbers
    actual_sum = sum(numbers)
    
    # The difference is the missing number
    missing_number = expected_sum - actual_sum
    
    if missing_number == 0:
        return "There is no missing number."
    else:
        return f"Missing number: {missing_number}"

def main():
    # Get input from the user
    user_input = input("Enter an array of numbers (separated by spaces):\n")
    
    # Convert the input into a list of integers
    numbers = list(map(int, user_input.split()))
    
    # Find and display the missing number
    result = find_missing_number(numbers)
    print(result)

if __name__ == "__main__":
    main()