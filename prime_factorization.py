# Prime Factorization
# Have the user enter a number and find all Prime Factors (if there are any) and display them.
# Limit: 1 000 000

def user_number():
    while True:
        try:
            n = int(input('Select a number (from 2 to 1 000 000): '))
            if 2<=n<=1000000:
                return n
            else:
                print('Out of range, please try again...')
        except:
            print('Invalid input, please try again...')

def all_primes(n):
    prime_lst = []
    for n in range(2,n+1):
        prime = True
        for i in range(2,n):
            if n%i == 0:
                prime = False
        if prime:
            prime_lst.append(n)
    print(prime_lst)

def testing():
    test1 = all_primes(7)
    test2 = all_primes(8)
    test3 = all_primes(13)
    test4 = all_primes(21)
#testing()

all_primes(user_number())
