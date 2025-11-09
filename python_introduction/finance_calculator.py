monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses:"))
interest_rate = 0.05

monthly_saving = monthly_income - monthly_expenses
annual_savings= monthly_saving * 12 + (monthly_saving * 12 * interest_rate)

print("Your annual savings including interest is:", annual_savings)


