# -*- coding: utf-8 -*-
balance = 320000
annualInterestRate = 0.2
def increment():

def getLowestPaymentBisection(balance, annualInterestRate):
    '''
    using bisection search 
    return: the lowest payment to pay off the balance within 12 months
        will be the multiple of $0.01
    '''

    def getRemainingBalance(balance, annualInterestRate, monthlyPayment):
        monthlyUnpaidBalance = balance - monthlyPayment
        monthlyUpdatedBalance = monthlyUnpaidBalance * ( 1 + annualInterestRate / 12 )
        return monthlyUpdatedBalance

    low = balance/12
    high = (balance * (1 + annualInterestRate/12.0)**12) / 12.0
    monthlyPayment = (low + high)/2
    epsilon = 0.01
    balance0 = balance
    while (high-low)/2>=epsilon:
        balance = balance0
        for m in range(1,13):
            balance = getRemainingBalance(balance, annualInterestRate, monthlyPayment)
        if balance > 0:
            low = monthlyPayment
        else:
            high = monthlyPayment
        monthlyPayment = (low + high)/2
    print('Lowest Payment:', round(monthlyPayment,2))

getLowestPaymentBisection(balance,annualInterestRate)
