current_budget = 3500.75

def print_remaining_budget(budget):
    print(f"Your remaining budget is: ${str(budget)}")

    print_remaining_budget(current_budget)

def deduct_expense(budget, expense):
    print(f"The budget = {budget}") 
    print(f"The expense = {expense}")
    return budget-expense

print(deduct_expense(current_budget, 5))
shirt_expense = 15

new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)

print_remaining_budget(new_budget_after_shirt)