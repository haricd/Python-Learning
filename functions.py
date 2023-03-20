def favColor():
    color = input("Enter your fav color : ")
    print(f"It seems your fav color is {color}")
favColor()

def welcome(name, clss):
    print(f"Welcome {name}, nice to meet you in {clss} class")
enter_name = input("Enter your name: ")
enter_class = input("Enter your subject: ")
welcome(enter_name, enter_class)

def dummy_fun(a,b):
    sum = a+b
    return sum
num1 = 5
num2 = 5
print(dummy_fun(num1, num2))
