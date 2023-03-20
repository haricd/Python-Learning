max_num = 5
counter = 0
while counter < max_num:
    counter += 1
    print(counter)

user_command = 'initial'
while user_command.lower() != 'python':
    user_command = input(">Command ur word :")
    print(user_command)
