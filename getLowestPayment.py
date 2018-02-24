# -*- coding: utf-8 -*-
balance = 999999
annualInterestRate = 0.18

def getLowestPayment(balance, annualInterestRate):
    '''
    return: the lowest payment to pay off the balance within 12 months
        will be the multiple of $10
    '''

    def getRemainingBalance(balance, annualInterestRate, minimalFixedMonthlyPayment):
        monthlyUnpaidBalance = balance - minimalFixedMonthlyPayment
        monthlyUpdatedBalance = monthlyUnpaidBalance * ( 1 + annualInterestRate / 12 )
        return monthlyUpdatedBalance

    minimalFixedMonthlyPayment = 90325.02
    balance0 = balance
    while True:
        balance = balance0
        for m in range(1,13):
            balance = getRemainingBalance(balance, annualInterestRate, minimalFixedMonthlyPayment)
        if balance <=0:
            break
        print('balance:',balance,'p: ',minimalFixedMonthlyPayment)
        minimalFixedMonthlyPayment +=0.01
    print('Lowest Payment:', minimalFixedMonthlyPayment,'b:',balance)

getLowestPayment(balance,annualInterestRate)
