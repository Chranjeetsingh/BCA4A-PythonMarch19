num = int(input("Enter the number "))

print(f"Multiplication of {num}:")
for i in range(1, 11):
    product = num * i
    print(f"{num} x {i} = {product}")