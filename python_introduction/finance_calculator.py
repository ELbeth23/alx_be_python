income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses:"))
interest_rate = 0.05

saving = income - expenses
annual_savings= saving * 12 + (saving * 12 * interest_rate)

print("Your annual savings including interest is:", annual_savings)


