def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))

if num < 0:
    print("Invalid input!")
else:
    result = factorial(num)
    print(f"Factorial of {num} is:", result)
