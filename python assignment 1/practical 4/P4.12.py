def is_even(num):
    return num % 2 == 0

count = 0
number = 2  

print("Cube of the first 10 even numbers:")
while count < 10:
    if is_even(number):
        cube = number ** 3
        print(f"{number}^3 = {cube}")
        count += 1
    number += 2 