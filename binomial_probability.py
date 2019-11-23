import math

def binomial():
    '''returns the probability of exactly k successes in n attempts'''

    n = int(input('Select number of trials: n = '))
    k = int(input('Select number successes: k = '))
    p = float(input('Select the probability of success of a single trial: p = '))
    result = (math.factorial(n) * p**k * (1-p)**(n-k)) / (math.factorial(k) * math.factorial(n-k))
    return '\nP(k={}) = {}\n'.format(k,result)

def atleast():
    '''returns the probability of event successes that happened 'at least k times' in n attempts'''

    n = int(input('Select number of trials: n = '))
    k = int(input('Select number of \'at least\' successes: k = '))
    p = float(input('Select the probability of success of a single trial: p = '))
    result = 0
    for i in range(k,n+1):
        result += (math.factorial(n) * p ** i * (1 - p) ** (n - i)) / (math.factorial(i) * math.factorial(n - i))
    return '\nP(k={}-{}) = {}\n'.format(k,n,result)

def atmost():
    '''returns the probability of event successes that happened 'at most k times' in n attempts'''

    n = int(input('Select number of trials: n = '))
    k = int(input('Select number of \'at most\' successes: k = '))
    p = float(input('Select the probability of success of a single trial: p = '))
    result = 0
    for i in range(k+1):
        result += (math.factorial(n) * p ** i * (1 - p) ** (n - i)) / (math.factorial(i) * math.factorial(n - i))
    return '\nP(k=0-{}) = {}\n'.format(k,result)

def probability():
    '''returns the result of binomial probability'''

    while True:
        try:
            user = input('Choose one of the following: \n- \'exactly\' k number of success\n- \'at least\' k number of success\n- \'at most\' k number of success\n...\n\n')
            if user.lower()[0] == 'e':
                result = binomial()
                return result
            elif user.lower()[3] == 'l':
                result = atleast()
                return result
            elif user.lower()[3] == 'm':
                result = atmost()
                return result
        except:
            print('Invalid input, try again...\n')

probability = probability()
print(probability)