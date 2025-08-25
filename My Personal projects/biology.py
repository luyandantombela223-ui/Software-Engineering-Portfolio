# determining the animal type using  biology
# Luyanda Ntombela
# 09 March 2025

print("Welcome to the Biology Expert")
print("------------------------------------------------------------------")
print("Answer the following questions by selecting from among the options.")
organism = input("Does the organism have a backbone? (yes/no):\n").lower() #backbone or not

if organism == 'yes':
    warmb = input("Is it warm-blooded? (yes/no):\n").lower() # type of blood in organism
    if warmb == 'yes' :
        feathers =input("Does it have feathers? (yes/no):\n").lower()# has feathers or nor
        if feathers == 'yes' :
            print("It is a Bird.") 
        if feathers == 'no' :
            fur = input("Does it have fur? (yes/no):\n").lower()
            if fur == 'yes' :
                print("It is a Mammal.")#name of organism
            if fur == 'no' :
                print("Other vertebrate")
                
    elif warmb == 'no' : 
        scales =input("Does it have scales? (yes/no):\n").lower()
        if scales == 'yes':
            print("It is a Reptile or Fish")
            aquatic = input("Does it live in water? (yes/no):\n").lower()
            if aquatic == 'yes' :
                print("It is a fish.")
            if aquatic == 'no' :
                print("It is a Reptile.")
        if scales == 'no':
            print("It is an Amphibian.")

if organism =='no' : 
    exeskeleton =input("Does it have an exoskeleton? (yes/no):\n").lower()
    if exeskeleton == 'yes' :
        six_leg = input("Does it have six legs? (yes/no):\n").lower()
        if six_leg == 'yes' :
                print("It is an Insect.")
        if six_leg == 'no' :
            eight_legs = input("Does it have eight legs? (yes/no):\n").lower()
            if eight_legs == 'yes' :
                print("It is an Arachnid.") #type of animal
            if eight_legs =='no' :
                print("Crustacean")
    if exeskeleton == 'no' :
        segmented_body = input("Does it have a segmented body? (yes/no):\n").lower()
        if segmented_body == 'yes' :
            print("It is an Annelid (e.g., Earthworm).")
        if segmented_body == 'no' :
            shell = input("Does it have a shell? (yes/no):\n").lower()
            if shell == 'yes' :
                print("It is a Snail or Clam.")
            if shell == 'no':
                print("It is an Octopus or Squid.")
            
                
    
