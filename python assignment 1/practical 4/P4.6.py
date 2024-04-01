def fibonacci_seq(n):
    fibonacci = [0, 1]

    for i in range(2, n):
        next_term = fibonacci[i - 1] + fibonacci[i - 2]
        fibonacci.append(next_term)

    return fibonacci

n = int(input("Enter value of n for Fibonacci sequence: "))

if n <= 0:
    print("Invalid input! enter a positive integer.")
else:
    sequence = fibonacci_seq(n)
    print("Fibonacci sequence to nth term:")
    print(sequence)
