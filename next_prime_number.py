# Next Prime Number
# Have the program find prime numbers until the user chooses to stop asking for the next one.
# Limit: 1 000 000

def user_number():
    '''User inputs the range to calculate from LOWEST to HIGHEST'''
    while True:
        # Lowest number
        try:
            low = int(input('Insert lowest number of range (2 - 999999): '))
            if 2<=low<=999999:
                break
            elif 2>low or low>999999:
                print('Out of range, please try again...')
                continue
        except:
            print('Invalid input, please try again...')
    while True:
        # Highest number
        try:
            high = int(input(f'Insert highest number of range ({low+1} - 1000000): '))
            if low < high <= 1000000:
                break
            elif low >= high:
                print(f'Your input must be higher than {low}, please try again...')
                continue
            elif high > 1000000:
                print('Out of range, please try again...')
                continue
        except:
            print('Invalid input, please try again...')
    return low,high

def all_primes(low,high):
    '''Prime number calculator, based on a range of numbers'''
    prime_lst = []
    for high in range(low,high+1):
        prime = True
        for i in range(2,high):
            if high%i == 0:
                prime = False
        if prime:
            prime_lst.append(high)
    return prime_lst

def list_full():
    '''List of all calculated prime numbers'''
    print('\nTask complete. The list of prime numbers within range {} is:\n{}'.format(prime_range, prime_list))

def list_partial():
    '''Interrupted list of calculated prime numbers'''
    print('\nTask interrupted...\nThe partial list of prime numbers within range {} until you stopped, is the following:\n{}'.format(prime_range, prime_list))

def main_code():
    '''Execution'''
    fulllist = False
    for num in all_primes(prime_range[0], prime_range[1]):
        if num == 2:
            print(f'\n- The first prime number is {num}')
            prime_list.append(num)
            continue
        elif num > 2:
            print(f'\n- The next prime number is {num}')
            prime_list.append(num)
        if num == prime_range[1]:
            print('You have reached the end\n')
            break
        user_input = input('  Continue? y/n: ')
        if user_input == 'y':
            fulllist = True
            continue
        elif user_input == 'n':
            list_partial()
            fulllist = False
            break
    if fulllist:
        list_full()

prime_list = []
prime_range = user_number()
print(f'The range you have selected is: {prime_range}')
main_code()



