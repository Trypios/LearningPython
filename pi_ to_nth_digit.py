# Calculate pi to the Nth Digit.
# Enter a number and have the program generate π (pi) up to that many decimal places.
# Keep a limit to how far the program will go. Limit set to 50 decimal digits.

# UNFINISHED !!!!!!!!!!
# Find a way to build a pi calculator to replace the pi string with.

def nth_digit():
    '''User defined n'''
    while True:
        try:
            n = int(input('How long do you want the Pi to be, in decimal digits? (range 2-50): \n'))
            if n <= 50 and n >= 2:
                return n
            else:
                print('Out of range, please try again...')
        except:
            print('Incorrect input, please try again...')

def pi_calc():
    pass

def pi_digits(n):
    '''Return result'''
    pi = '3.1415926535897932384626433832795028841971693993751058209'
    return 'The Pi up to {} decimal digits is: {}'.format(n,pi[:n+2])

test_pi = pi_digits(nth_digit())
print(test_pi)
