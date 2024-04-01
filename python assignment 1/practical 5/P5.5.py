my_list = [10, 20, 30, 40, 50]

print("Original list:", my_list)

#Append method
my_list.append(60)
print("List after appending 60:", my_list)

#Insert method
my_list.insert(2, 15)
print("List after inserting 15 at index 2:", my_list)

#Remove method
my_list.remove(30)
print("List after removing 30:", my_list)

#Pop method
popped_element = my_list.pop(3)
print("Popped element at index 3:", popped_element)
print("List after popping element at index 3:", my_list)

# Index method
index_of_50 = my_list.index(50)
print("Index of 50:", index_of_50)

#Count method
count_of_20 = my_list.count(20)
print("Count of 20:", count_of_20)

#Sort method
my_list.sort()
print("List after sorting in ascending order:", my_list)

#Reverse method
my_list.reverse()
print("List after reversing:", my_list)

#Clear method
my_list.clear()
print("List after clearing:", my_list)