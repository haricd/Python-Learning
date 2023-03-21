list_ex = [3,6,1,7,4,9]
list_ex.sort()
print(list_ex)

var_list = ['monkey', 'donkey', 'ant', 'elephant', 'dog']
var_list.sort()
print(var_list) 

var1_list = ['monkey', 'donkey', 'ant', 'elephant', 'dog']
var1_list.sort(reverse=True)
print(var1_list)

list_tuples = [('Google', 2019, 134.81), ('Apple', 2019, 26.2), ('Facebook', 2019, 70.7)]
list_tuples.sort(key=lambda company: company[2], reverse=True)
print(list_tuples)
