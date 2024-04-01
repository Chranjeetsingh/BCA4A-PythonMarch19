
demo = "Hello"

print("Original string:", demo)

length = len(demo)
print("Length of the string:", length)

uppercase_string = demo.upper()
print("Uppercase string:", uppercase_string)

lowercase_string = demo.lower()
print("Lowercase string:", lowercase_string)

capitalized_string = demo.capitalize()
print("Capitalized string:", capitalized_string)

count_e = demo.count('e')
print("Count of 'e' in the string:", count_e)

index_world = demo.find('World')
print("Index of 'World':", index_world)

replaced_string = demo.replace('demo', 'example')
print("String after replacement:", replaced_string)

split_string = demo.split(',')
print("Split string:", split_string)
