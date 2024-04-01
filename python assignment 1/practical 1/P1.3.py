    #formula: A = P(1 + r/n)^(nt)
    #A is the amount, P is the principal amount, r is the annual interest rate
    # n is number of times interest is compounded per year, and t is the time in years.

def calc_compound_interest(principal, rate, time):
    
    n = 12
    amount = principal * (1 + rate / (n * 100))**(n * time)
    compound_interest = amount - principal
    return compound_interest

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (%): "))
time = float(input("Enter the time period in years: "))

interest = calc_compound_interest(principal, rate, time)

print(f"The compound interest is: {interest}")
