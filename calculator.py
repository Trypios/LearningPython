# SIMPLE CALCULATOR

# TWO NUMBER OPS:
# add (+), subtract (-), multiply (*), divide (/)
# ONE NUMBER OPS:
# swap sign (+-), exponent, root, ln, log, factorial

import math
import time

history_list = []
op_simple_list = ['+', '-', '*', '/']
op_complex_list = ['swap', 'exp', 'root', 'ln', 'log', 'n!']

def intro():
    '''Simple introduction'''
    print('\n!! MATH CALCULATOR !!\n')
    print('Choose what would you like to do by selecting the corresponding symbol of the following:\n')
    time.sleep(1.5)

def intro_ops():
    '''Show the user the operator symbols'''
    print('\n- Add two numbers (+)')
    print('- Subtract two numbers (-)')
    print('- Multiply two numbers (*)')
    print('- Divide two numbers (/)\n')
    print('- Swap the sign of a number (swap)')
    print('- Calculate exponent of a number (exp)')
    print('- Calculate the root of a number (root)')
    print('- Calculate the natural log of a number (ln)')
    print('- Calculate the logarithm base10 of a number (log)')
    print('- Calculate the factorial of a number (n!)')

def operator():
    while True:
        op = input('\nSelect symbol of operator: ')
        if op in op_simple_list or op in op_complex_list:
            return op
        else:
            print('\n' * 30)
            print('\nThere must have been a typo, please try again from the following list of operators:\n')
            intro_ops()

def calc_add():
    print('\nYou have selected to add (+) two numbers.\n')
    while True:
        try:
            x = float(input('Insert the first Number: '))
            break
        except:
            print('Invalid input, please try again...')
    while True:
        try:
            y = float(input('Insert the second Number: '))
            break
        except:
            print('Invalid input, please try again...')
    print('\n{} + {} = {}\n'.format(x, y, x + y))
    return x+y

def calc_add2():
    x = history_list[-1]
    print('\nYou have selected to add (+) {} to a new number.\n'.format(x))
    while True:
        try:
            y = float(input('Insert the second Number: '))
            break
        except:
            print('Invalid input, please try again...')
    print('\n{} + {} = {}\n'.format(x, y, x + y))
    return x+y

def calc_subtract():
    print('\nYou have selected to subtract (-) two numbers.\n')
    while True:
        try:
            x = float(input('Insert the first Number: '))
            break
        except:
            print('Invalid input, please try again...')
    while True:
        try:
            y = float(input('Insert the second Number: '))
            break
        except:
            print('Invalid input, please try again...')
    print('\n{} - {} = {}\n'.format(x,y,x-y))
    return x-y

def calc_subtract2():
    x = history_list[-1]
    print('\nYou have selected to subtract (-) a new number from {}.\n'.format(x))
    while True:
        try:
            y = float(input('Insert the second Number: '))
            break
        except:
            print('Invalid input, please try again...')
    print('\n{} - {} = {}\n'.format(x,y,x-y))
    return x-y

def calc_multiply():
    print('\nYou have selected to multiply (*) two numbers.\n')
    while True:
        try:
            x = float(input('Insert the first Number: '))
            break
        except:
            print('Invalid input, please try again...')
    while True:
        try:
            y = float(input('Insert the second Number: '))
            break
        except:
            print('Invalid input, please try again...')
    print('\n{} * {} = {}\n'.format(x,y,x*y))
    return x*y

def calc_multiply2():
    x = history_list[-1]
    print('\nYou have selected to multiply (*) {} with a new number.\n'.format(x))
    while True:
        try:
            y = float(input('Insert the second Number: '))
            break
        except:
            print('Invalid input, please try again...')
    print('\n{} * {} = {}\n'.format(x,y,x*y))
    return x*y

def calc_divide():
    print('\nYou have selected to divide (/) two numbers.\n')
    while True:
        try:
            x = float(input('Insert the first Number: '))
            break
        except:
            print('Invalid input, please try again...')
    while True:
        try:
            y = float(input('Insert the second Number: '))
            if y == 0:
                print('Never divide by zero, please try again...')
                continue
            else:
                break
        except:
            print('Invalid input, please try again...')
    print('\n{} / {} = {}\n'.format(x,y,x/y))
    return x/y

def calc_divide2():
    x = history_list[-1]
    print('\nYou have selected to divide (/) {} with a new number.\n'.format(x))
    while True:
        try:
            y = float(input('Insert the second Number: '))
            if y == 0:
                print('Never divide by zero, please try again...')
                continue
            else:
                break
        except:
            print('Invalid input, please try again...')
    print('\n{} / {} = {}\n'.format(x,y,x/y))
    return x/y

def calc_swap():
    print('\nYou have selected to swap the sign of a number.\n')
    while True:
        try:
            x = float(input('Insert the Number: '))
            break
        except:
            print('Invalid input, please try again...')
    print('\nresult: {}\n'.format(x*(-1)))
    return x*(-1)

def calc_swap2():
    x = history_list[-1]
    print('\nYou have selected to swap the sign of {}.\n'.format(x))
    print('\nResult: {}\n'.format(x*(-1)))
    return x*(-1)

def calc_exp():
    print('\nYou have selected to calculate the exponent of a number.\n')
    while True:
        try:
            x = float(input('Insert the Number: '))
            break
        except:
            print('Invalid input, please try again...')
    while True:
        try:
            y = float(input('To what power will this number be raised to? '))
            break
        except:
            print('Invalid input, please try again...')
    print('\n{} to the power of {} = {}\n'.format(x,y,x**y))
    return x**y

def calc_exp2():
    x = history_list[-1]
    print('\nYou have selected to calculate the exponent of {}.\n'.format(x))
    while True:
        try:
            y = float(input('To what power will this number be raised to? '))
            break
        except:
            print('Invalid input, please try again...')
    print('\n{} to the power of {} = {}\n'.format(x,y,x**y))
    return x**y

def calc_root():
    print('\nYou have selected to calculate the root of a number.\n')
    while True:
        try:
            x = float(input('Insert a positive number: '))
            if x < 0:
                print('The root of a negative number, results in irrational number, please try again...')
            else:
                break
        except:
            print('Invalid input, please try again...')
    while True:
        try:
            y = int(input('Choose radical:\n- type 2 for square root\n- or 3 for cube root\n- or other radical...\n '))
            break
        except:
            print('Invalid input, please try again...')
    if y == 2:
        print('\nSquare root of {} = {}\n'.format(x, x ** (1 / y)))
    elif y == 3:
        print('\nCube root of {} = {}\n'.format(x, x ** (1 / y)))
    else:
        print('\n{}th root of {}  {:.2f}\n'.format(y, x, x ** (1 / y)))
    return x ** (1/y)

def calc_root2():
    x = history_list[-1]
    if x < 0:
        print('\n{} is negative and will result to an irrational number. Try a different operator...\n'.format(x))
        return
    else:
        print('\nYou have selected to calculate the root of {}.\n'.format(x))
    while True:
        try:
            y = int(input('Choose radical:\n- type 2 for square root\n- or 3 for cube root\n- or other radical...\n '))
            break
        except:
            print('Invalid input, please try again...')
    if y == 2:
        print('\nSquare root of {} = {}\n'.format(x, x ** (1 / y)))
    elif y == 3:
        print('\nCube root of {} = {}\n'.format(x, x ** (1 / y)))
    else:
        print('\n{}th root of {}  {:.2f}\n'.format(y, x, x ** (1 / y)))
    return x ** (1 / y)

def calc_ln():
    print('\nYou have selected to calculate the natural log (ln) of a number.\n')
    while True:
        try:
            x = float(input('Insert the Number: '))
            if x < 0:
                print('\n{} is negative, natural log only works for positive numbers. Try a different operator...\n'.format(x))
            else:
                break
        except:
            print('Invalid input, please try again...')
    result = math.log1p(x)
    print('\nln({}) = {}\n'.format(x, result))
    return result

def calc_ln2():
    x = history_list[-1]
    if x < 0:
        print('\n{} is negative, natural log only works for positive numbers. Try a different operator...\n'.format(x))
        return
    else:
        print('\nYou have selected to calculate the natural log (ln) of number {}.\n'.format(x))
    result = math.log1p(x)
    print('\nln({}) = {}\n'.format(x, result))
    return result

def calc_log():
    print('\nYou have selected to calculate the log with base 10 of a number.\n')
    while True:
        try:
            x = float(input('Insert the Number: '))
            if x < 0:
                print('\n{} is negative, natural log only works for positive numbers. Try a different operator...\n'.format(x))
            else:
                break
        except:
            print('Invalid input, please try again...')
    result = math.log10(x)
    print('\nlog({}) = {}\n'.format(x, result))
    return result

def calc_log2():
    x = history_list[-1]
    if x < 0:
        print('\n{} is negative, logarithms only works for positive numbers. Try a different operator...\n'.format(x))
        return
    else:
        print('\nYou have selected to calculate the log with base 10 of number {}.\n'.format(x))
    result = math.log10(x)
    print('\nlog({}) = {}\n'.format(x, result))
    return result

def calc_fctr():
    print('\nYou have selected to calculate the factorial (n!) of a number.\n')
    while True:
        try:
            x = int(input('Insert the Number (positive integers only): '))
            if x <= 0:
                print('Factorial numbers cannot be negative')
            else:
                break
        except:
            print('Invalid input, please try again...')
    if x == 0:
        print('\n{}! = {}\n'.format(x, 1))
        return 1
    else:
        n = 1
        for i in range(1,x+1):
            n *= i
        print('\n{}! = {}\n'.format(x, n))
        return n

def calc_fctr2():
    x = history_list[-1]
    print('\nYou have selected to calculate the factorial (n!) of number {}.\n'.format(x))
    if x%1 != 0:
        print('\nThis number is not an integer. Factorial only works for positive integers. Please select a different operator...')
    elif x == 0:
        print('\n{}! = {}\n'.format(x, 1))
        return 1
    else:
        n = 1
        for i in range(1,x+1):
            n *= i
        print('\n{}! = {}\n'.format(x, n))
        return n

def cont():
    while True:
        userinput = input('Continue? y/n: ')
        if userinput[0].lower() == 'y':
            return True
        if userinput[0].lower() == 'n':
            return False
        else:
            print('Invalid input, please try again...')

def main():
    global history_list
    history_list = []
    intro()
    intro_ops()
    op = operator()
    # if two number ops:
    while op in op_simple_list:
        if op == '+':
            history_list.append(calc_add())
        elif op == '-':
            history_list.append(calc_subtract())
        elif op == '*':
            history_list.append(calc_multiply())
        elif op == '/':
            history_list.append(calc_divide())
        break
    # if one number ops:
    while op in op_complex_list:
        if op == 'swap':
            history_list.append(calc_swap())
        elif op == 'exp':
            history_list.append(calc_exp())
        elif op == 'root':
            history_list.append(calc_root())
        elif op == 'ln':
            history_list.append(calc_ln())
        elif op == 'log':
            history_list.append(calc_log())
        elif op == 'n!':
            history_list.append(calc_fctr())
        break
    #func to continue:
    while cont():
        intro_ops()
        op = operator()
        # if two number ops:
        while op in op_simple_list:
            if op == '+':
                history_list.append(calc_add2())
            elif op == '-':
                history_list.append(calc_subtract2())
            elif op == '*':
                history_list.append(calc_multiply2())
            elif op == '/':
                history_list.append(calc_divide2())
            break
        while op in op_complex_list:
            if op == 'swap':
                history_list.append(calc_swap2())
            elif op == 'exp':
                history_list.append(calc_exp2())
            elif op == 'root':
                history_list.append(calc_root2())
            elif op == 'ln':
                history_list.append(calc_ln2())
            elif op == 'log':
                history_list.append(calc_log2())
            elif op == 'n!':
                history_list.append(calc_fctr2())
            break
if __name__ == '__main__':
    main()

