# A code to find subsets of the given input
# Luyanda Ntombela
# 01 May 2025

def power_set(s):
    # Base case: empty set has one subset - the empty list
    if not s:
        return [[]]
    else:
        first = s[0]
        rest = s[1:]
        subsets_without_first = power_set(rest)
        subsets_with_first = add_element_to_subsets(first, subsets_without_first)
        return subsets_without_first + subsets_with_first

def add_element_to_subsets(element, subsets):
    # Recursively add element to each subset
    if not subsets:
        return []
    else:
        first_subset = subsets[0]
        rest_subsets = subsets[1:]
        new_subset = [element] + first_subset
        return [new_subset] + add_element_to_subsets(element, rest_subsets)

def main():
    user_input = input("Enter elements of the set separated by spaces:\n")
    elements = user_input.split()
    result = power_set(elements)
    print(f"There are {len(result)} subsets.")
    print("The subsets making up the power set are:")
    print_subsets(result)

def print_subsets(subsets):
    # Recursively print each subset
    if not subsets:
        return
    else:
        first = subsets[0]
        rest = subsets[1:]
        print(first)
        print_subsets(rest)

if __name__ == "__main__":
    main()
