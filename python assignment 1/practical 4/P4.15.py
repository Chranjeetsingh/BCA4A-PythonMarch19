
def create_and_sort_list(size):
    print("Enter elements for the list:")
    my_list = []
    for i in range(size):
        element = int(input(f"Enter element {i+1}: "))
        my_list.append(element)
    
    print("List before sorting:", my_list)
    
    my_list.sort()
    
    print("List after sorting in ascending order:", my_list)

size = int(input("Enter the size of the list: "))

create_and_sort_list(size)
