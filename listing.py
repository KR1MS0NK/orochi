numbers = [1, 2, 3, 4, 5, 6]
names = ["alice", "danso", "bea","fredos"]
print(numbers)
print(names)#print entire array
print(names[2])#print index char 2 from array, start 0
print(names[-3])#print index from the right,start -1
print(numbers[2:])#print index 2 to last
print(numbers[2:5])#print index 2 to 5-1
names.extend(numbers)
print(names)

#tuples = cant be modified in any way after it hs been iniialized
nums = (2,  3, 4, 5)