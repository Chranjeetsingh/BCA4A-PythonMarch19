basic_salary = float(input("Enter the basic salary: "))

if basic_salary >= 20000:
    da = 0.3 * basic_salary
    hra = 0.2 * basic_salary
else:
    da = 0.2 * basic_salary
    hra = 0.1 * basic_salary

total_salary = basic_salary + da + hra

print(f"Basic Salary: {basic_salary}")
print(f"DA: {da}")
print(f"HRA: {hra}")
print(f"Total Salary: {total_salary}")