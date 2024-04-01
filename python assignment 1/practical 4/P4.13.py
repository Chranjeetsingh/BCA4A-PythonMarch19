n = int(input("Enter positive integer: "))

if n <= 0:
    print("Invalid input!")
else:
    sum_natural = (n * (n + 1)) // 2

    print(f"Sum of the first {n} natural numbers is:", sum_natural)
