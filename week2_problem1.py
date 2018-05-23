balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


index = 0

while index < 12:	      
    month = annualInterestRate / 12

    month_min = monthlyPaymentRate * balance

    unpaid = balance - month_min

    new_balance = round (unpaid + (month * unpaid) , 2)
    
    index = index +1
    
    balance = new_balance
    
print ("Remaining balance: " + str(new_balance) )



