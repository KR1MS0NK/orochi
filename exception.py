#try except- for handling wrong input
try:
    num = int(input("enter a number"))
    print(num)
    
except:
    print("invalid input")



#opening file in python read write

random = open("example.txt", "r") #to read , w to write , a to append, r+ to read and write
print(random.read())# read the whole thing
print(random.readline())#read 1st line
print(random.readline())#read 2nd line you see the trend here,
print(random.readlines())# converts document to array and reads it
print(random.readlines()[1])#reads text in array with index 1
random.close()