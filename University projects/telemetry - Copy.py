# collecting important of driver vehicle things from user input
# Luyanda Ntombela
# 13 April 2025

def get_data_block(raw_data): # a function to exctract the substring
    start = raw_data.find("START") + 5  #adding 5 since length of START is 5
    end = raw_data.find("END") # finding where the is 'END'
    return raw_data[start:end].strip()

def rpm(data_block): # a function to get engine nmber
    start = data_block.find(':') + 1  #finding a colon since speed is found in front  of the first colon
    end =  data_block.find('|') #finding where it does ends
    return data_block[start:end]

def speed(data_block): # a function to find speed
    start = data_block.find('|')+1
    end = data_block.find('l')  -1
    return data_block[start:end]

def coordinates(data_block):
    start = data_block.find('=')+1  # finding first = sign
    end = data_block.find('=',start+1)-5
    data_block[start:end]
    start2 = data_block.find('=',start+1)+1 #finding the second = sign
    end2 = data_block.find('=',start2 + 1) - 5 #finding third = sign
    lat = data_block[start:end]
    long =data_block[start2:end2]
    return (eval(lat),eval(long)) # answer in coordiinate form

def driver_name(data_block): #a function to get driver name
    start = data_block.find('name')+5
    end = len(data_block)
    return data_block[start:end]

def main():
    raw_data = input('Enter the raw data:\n') # input from the user
    data_block = get_data_block(raw_data)
    print("Vehicle Black Box Information:")
    print("Engine RPM:",rpm(data_block))
    print("Vehicle speed:",speed(data_block),end='km/h\n') 
    print("Coordinates:",(coordinates(data_block)))
    print("Driver's name:",driver_name(data_block))
    
if __name__=="__main__":
    main()