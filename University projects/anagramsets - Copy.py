# writes sets of anagrams of a certain length to a file
# Luyanda Ntombela
# 14 May 2025

def build_letter_count(word):
    """Returns letter count dictionary for the given word."""
    d = {}
    for c in word:
        d[c] = d.get(c, 0) + 1
    return d

print("***** Anagram Set Search *****")
try:
    length = int(input("Enter word length:\n"))
    print("Searching...")

    with open("EnglishWords.txt", "r") as f:
        line = f.readline()
        while line.strip() != "START":
            line = f.readline()
        words = [w.strip().lower() for w in f if len(w.strip()) == length]

    # Group words by sorted letter tuple
    anagram_dict = {}
    for word in words:
        key = tuple(sorted(word))
        if key not in anagram_dict:
            anagram_dict[key] = []
        if word not in anagram_dict[key]:
            anagram_dict[key].append(word)

    # Get sets with more than one word
    anagram_sets = [sorted(val) for val in anagram_dict.values() if len(val) > 1]

    # Sort alphabetically by first word in each set
    anagram_sets.sort(key=lambda x: x[0])

    filename = input("Enter file name:\n")
    print("Writing results...")

    with open(filename, "w") as out:
        for group in anagram_sets:
            out.write(str(group) + "\n")

except FileNotFoundError:
    print("Sorry, could not find file 'EnglishWords.txt'.")
