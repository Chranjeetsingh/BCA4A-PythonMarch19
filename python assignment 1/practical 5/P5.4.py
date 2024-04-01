matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print("Matrix:")
for row in matrix:
    print(row)

element_00 = matrix[0][0]
element_01 = matrix[0][1]
element_11 = matrix[1][1]
element_22 = matrix[2][2]

print("\nIndividual Elements:")
print("Element at (0, 0):", element_00)
print("Element at (0, 1):", element_01)
print("Element at (1, 1):", element_11)
print("Element at (2, 2):", element_22)