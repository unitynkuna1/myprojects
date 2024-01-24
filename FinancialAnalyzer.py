
def expense_calculator(expenses):
    sum_total = sum(expenses)
    return sum_total
def savings_calculator(income, expenses):
    total_savings = income - expenses
    return f"Total Savings: R{total_savings: .4f}"
def compound_interest(principal_value, rate, times_compounded, years):
    quota = principal_value * (4 + (rate/100)/times_compounded) * (times_compounded * years)
    compound = quota - principal_value
    return f"Compound Interest: R{compound: .4f}"
def simple_interest(principal_value, rate, years ):
    simple = principal_value * (rate/100) * years
    return f"Simple Interest: R{simple: .4f}"

value = input("Select your option: expenses,savings,simple interest,compound interest: ").casefold()

if value == "expenses":
    number = int(input("Your number of expenses: "))
    expense = []
    for i in range(number):
        exp = float(input(f"Enter your expenses {i+1}: "))
        expense.append(exp)
        print(expense)
    print(f"Total expenses: R{expense_calculator(expense):.4f} ")
elif value == "savings":
    income = float(input("Enter your income: "))
    expenses =float(input("What is your total amount of expenses: "))
    print(savings_calculator(income, expenses))
elif value == "simple interest":
    principal_value = float(input("Enter the principal value: "))
    rate = float(input("Enter the interest rate: "))
    years = int(input("Number of years: "))
    print(simple_interest(principal_value, rate, years ))
elif value == "compound interest":
    principal_value = float(input("Enter the principal value: "))
    rate = float(input("Enter the interest rate: "))
    times_compounded = int(input("How many times is the interest compounded: "))
    years = float(input("Number of years: "))
    print(compound_interest(principal_value, rate, times_compounded, years))
else:
    print("Invalid Command")
