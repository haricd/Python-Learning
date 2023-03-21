def recur(num):
    print(num)
    next = num - 1
    if next > 0:
        recur(next) 
recur(3)

# sequence of numbers

def sequnece(n):
    if n > 0:
        return n + sequnece(n-1)
    return 0
print(sequnece(3))
