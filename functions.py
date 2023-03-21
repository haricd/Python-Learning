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

# default paramter functions
def msg(message='hello world'):
    return message
out_put = msg()
print(out_put)

def msg2(name = "Hi Hari", message = "hello world"):
    return f"{name} {message}"
out_put = msg2("Hi Jaffer", "Hello country")
print(out_put)

def msg3(name = "Hi Hari", message = 'hello world'):
    return f"{name} {message}"
out_put = msg3(message="Hello country")
print(out_put)

# default argument functions
def msg4(name, message):
    return f"{name} {message}"
out_put = msg4("hari", "Hello country")
print(out_put)

def msg4(name, message):
    return f"{name} {message}"
out_put = msg4("hari", message= "Hello country")
print(out_put)


