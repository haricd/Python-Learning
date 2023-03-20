# for num in range(6):
#     print(num)
#     if num == 4:
#         break
#     print(num, 'last')

# for x in range(5):
#     for y in range(5):
#         if y > 1:
#             break
#         print(f"({x},{y})")

print(">>Help! Enter Stop to quit")
while True:
    user_inp = input("Enter Your Fav Color : ")
    if user_inp.lower() == "quit":
        print("You have successfully exited")
        break
    print(user_inp)