#Create a list
my_list = [10, 20, 30, 40, 50]

#Print list
print("Original list:", my_list)

#Access elements using index
print("First element:", my_list[0])
print("Last element:", my_list[-1])

# Modify elements
my_list[1] = 25
print("Modified list:", my_list)

#Append and remove elements
my_list.append(60)
my_list.remove(30)
print("List after appending 60 and removing 30:", my_list)

#Get length of list
length = len(my_list)
print("Length of the list:", length)

#Iterate through the list
print("Elements of the list:")
for num in my_list:
    print(num)

# Check if an element exists
if 40 in my_list:
    print("40 is present in the list")
else:
    print("40 is not present in the list")