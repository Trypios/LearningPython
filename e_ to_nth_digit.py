# Calculate e to the Nth Digit.
# Enter a number and have the program generate e up to that many decimal places.
# Keep a limit to how far the program will go. Limit set to 50 decimal digits.

# UNFINISHED !!!!!!!!!!
# Find a way to build an e calculator to replace the e string with.

def nth_digit():
    while True:
        try:
            n = int(input('Choose the length of e, in decimal digits (range 2-50): \n'))
            if 2<=n<=50:
                return n
            else:
                print('Out of range, please try again...')
        except:
            print('Invalid input, please try again...')

def e_calc():
    pass

def e_digits(n):
    e = '2.7182818284590452353602874713526624977572470936999595749'
    return 'The e number up to {} decimal digits is: {}'.format(n,e[:n+2])

test_e = e_digits(nth_digit())
print(test_e)