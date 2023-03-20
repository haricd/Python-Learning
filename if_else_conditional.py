# if...else comdition
user_input = input("Could you please enter your age: ")
if int(user_input) >= 18 :
    print("You are eligible to vote!")
else :
    print("Sorry your age is under age for voting")    

#if..elif..else condition
input_user = input("Tell me your age for ticket booking : ")
check = int(input_user)
if check <= 5 :
    tick_price = 25
elif check <= 13 :
    tick_price = 50
elif check <= 17 :
    tick_price = 75
elif check <= 25 :
    tick_price = 100
else:
    tick_price = 150
print(f"Your ticket price is {tick_price}")

#ternary operator
sample = 100 if int(user_input) > 18 else 50
print(sample)