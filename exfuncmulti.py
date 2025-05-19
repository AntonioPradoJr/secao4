def multiply(*args):
    res = 1
    for number in args:
        res *= number
    return res

def evenodd(x):
    if x %2 == 0:
        return f'The number {x} is even'
    
    return f'The number {x} is odd'


print(evenodd(3))