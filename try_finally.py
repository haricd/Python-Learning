a = 10
b = 2

try:
    c = a/b
    print(c)
except Exception as error:
    print(error)
finally:
    print("Finished")

print('########################################################################')

a = 10
b = 0

try:
    c = a/b
    print(c)
except Exception as error:
    print(error)
finally:
    print("Finished")