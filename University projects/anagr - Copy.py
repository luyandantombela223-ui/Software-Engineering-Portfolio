file = open("EnglishWords.txt","r")
lst1 = file.readlines()
file.close()
    
try:
    inpt = list(input("Enter a word: ").lower())
    sorted_input = sorted(inpt)
    s = []
    for i in lst1:
        k = list(i.strip().lower())  # Convert word to list and remove newline
        k.sort()  # Sort characters
        if k == sorted_input :
            s.append(i[:-1])        
    print("***** Anagram Finder ***** ")   
    del s[0]
    if s == []:
        print(f"Sorry, anagrams of '{''.join(inpt)}' could not be found.") 
    else:
        print(s)
except:
    print("Sorry, could not find file 'EnglishWords.txt'.")
