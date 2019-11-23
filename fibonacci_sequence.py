# Fibonacci sequence calculator
# Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.
# Limit is 50 numbers

def fib_func(n):
    '''Calculate Phi, append result to list'''
    x = 0
    y = 1
    lst = [0]
    for i in range(1,n):
        x,y = y,x+y
        lst.append(x)
    return lst

def nth_digit():
    '''User defined n'''
    while True:
        try:
            n = int(input('How long do you want the Pi to be, in decimal digits? (range 1-50: \n'))
            if n <= 50 and n >= 1:
                return n
            else:
                print('Out of range, please try again...')
        except:
            print('Incorrect input, please try again...')

result = ' '.join(str(e) for e in fib_func(nth_digit()))
print(result)
#0 1 1 2 3 5 8 13 21
