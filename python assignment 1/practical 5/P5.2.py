my_list = ['q', 'w', 'e', 'r', 't', 'y']

for index, element in enumerate(my_list):
    print(f"'{element}' at positive index {index} and negative index {-len(my_list) + index}")