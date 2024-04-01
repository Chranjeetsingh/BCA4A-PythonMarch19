num_list = [15, 22, 18, 20, 25, 19, 23]

mean = sum(num_list) / len(num_list)
print("Mean:", mean)

variance = sum((x - mean) ** 2 for x in num_list) / len(num_list)
print("Variance:", variance)

std_deviation = variance ** 0.5
print("Standard Deviation:", std_deviation)