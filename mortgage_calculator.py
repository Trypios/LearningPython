# Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate.
# Also figure out how long it will take the user to pay back the loan.

def loan_info():
    # Principal (initial cost):
    while True:
        try:
            P = int(input('What is the initial amount of mortgage? ...'))
            break
        except:
            print('Invalid input, please try again...')

    # Monthly interest (calculated by dividing your annual interest rate by 12):
    while True:
        try:
            r = float(input('What is the interest rate in percentage(%)? ...'))
            break
        except:
            print('Invalid input, please try again...')

    # Number of payments (the number of months you will be paying the loan):
    while True:
        try:
            n = int(input('How many months is the mortgage term? ...'))
            break
        except:
            print('Invalid input, please try again...')

    r /= 100
    infolist = [P,r,n]
    return infolist

def loan_func(P,r,n):
    # P = Principal (initial cost):
    # r = Monthly interest (calculated by dividing your annual interest rate by 12):
    # n = Installments (the number of months you will be paying the loan):

    # Monthly Payment Calculation:
    M = P * ((r * ((1 + r)**n))/(((1 + r)**n)-1))
    print('\nIt will take €{:.2f} per month for {} months to pay this mortgage of €{} at a {:.1f}% interest rate'.format(M,n,P,r*100))

P,r,n = loan_info()
loan_func(P,r,n)
