def calculate_tax(salary):
    # Tax brackets and rates
    brackets = [41667, 41667, 41667, 41667,41667, float('inf')]
    rates = [0.06, 0.12, 0.18, 0.24, 0.30, 0.36]

    remaining_salary = max(0, salary - 100000)  # Consider income above 100,000 only
    total_tax = 0

    for i in range(len(brackets)):
        if remaining_salary > 0:
            current_bracket = min(brackets[i], remaining_salary)
            current_rate = rates[i]
            tax_in_bracket = current_bracket * current_rate
            total_tax += tax_in_bracket
            remaining_salary -= current_bracket

    return total_tax

# Example usage:
salary_amount = float(input("Enter the salary amount: "))
tax_amount = calculate_tax(salary_amount)

if salary_amount > 100000:
    print(f'Tax for a salary of {salary_amount:.2f} is {tax_amount:.2f}')
else:
    print('Tax is not applicable for income less than 100,000.')
