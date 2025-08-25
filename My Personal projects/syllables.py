# the program counting the syllables in the word
# Luyanda Ntombela
# 14 April 2025

def count_syllables(word): # a function to count the number of syllables in the word
    vowels = 'aeiouy' #The letters that contributes on making sylables
    count = 0  # inintializing our count value
    for i in word:
        if i in vowels:
            count += 1  # add or increment one if i in vowels 
    for i in range(len(word)-1):
        if word[i] in vowels and word[i+1] in vowels:
            count -=1 # decrement one if the letters are consecutive
    if word[-1] == 'e' in vowels and word[-2] in vowels:
        count += 1
    if word[-1] == 'e':
            count -= 1 # decrement one if the last letter is e
    if count < 1 :
        count = 1 # count cannot be less then one
    return count

def main():
    word = input("Enter a word (or 'q' to quit):\n") # input from the user
        
    count = count_syllables(word)
    if word == 'q': # if a user enter 'q' exit the code
        exit() 
    while word != 'q': # do this if a user didn't enter 'q'
        if count == 1 :
            print("The word '" + word +"' has",count,"syllable.")
    
        else:
            print("The word '" + word +"' has",count,"syllables.")
        print()
        word = input("Enter a word (or 'q' to quit):\n") # repeat this loop until user enter 'q'
        count = count_syllables(word)
if __name__ == '__main__' :
    main()
