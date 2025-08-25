
file = open('EnglishWords.txt','r')
objects = file.readlines()
file.close()

def check():
    word = ''
    for i in range(len(objects)-1):
        f = objects[i].strip()
        j = objects[i+1].strip()
        
        for a in f:
            for b in j:
                word += b  # still not a useful operation

        print(f"f: {f}, j: {j}, word: {word}")  # Debug output

        if len(f) == len(j):
            if len(f) - len(word) == 1:
                return f, j
    return None

