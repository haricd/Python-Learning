user_input = input("Enter your salary amount: ")

expense_input = input("Enter your Expenses amount: ")

cals_int = int(user_input) - int(expense_input)

cals_float = float(user_input) - float(expense_input)

cals_bool = bool(user_input) 

print(f"""So your balance amount in integer is: {cals_int}
So your balance amount in float is: {cals_float}
So your balance amount in bool is: {cals_bool}""")





