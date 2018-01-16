# -*- coding: utf-8 -*-
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

def getMonthlyBalance(balance, annualInterestRate, monthlyPaymentRate):
    '''
    return: the remaining balance at the end of the month
    '''
    minimalPayment = balance*monthlyPaymentRate
    monthlyUnpaidBalance = balance - minimalPayment
    interest = monthlyUnpaidBalance*annualInterestRate/12
    return monthlyUnpaidBalance + interest

def getFinalBalance(balance, annualInterestRate, monthlyPaymentRate):
    for m in range(12):
        balance = getMonthlyBalance(balance, annualInterestRate, monthlyPaymentRate)
    remainingBalance = round(balance,2)
    print('Remaining balance:',remainingBalance)

getFinalBalance(balance,annualInterestRate,monthlyPaymentRate)
