rate = input("What is the interest rate? ")
rate = float(rate)

mortgage = input("How much is your mortgage? ")
mortgage = float(mortgage)

years = input("What is the amortization period? ")
years = int(years)

# Calculations
MonthlyRate = rate / 12
#AnswerMonthlyRate = int(rate)

NumberofPayments = years / 12

#need to figure out calculation for monthly mortgage payments
MonthlyPayments = NumberofPayments * MonthlyRate

# Answers
print(MonthlyPayments)





