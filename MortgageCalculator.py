rate = input("What is the interest rate? ")
rate = float(rate)/100/12

mortgage = input("How much is your mortgage? ")
mortgage = float(mortgage)

years = input("What is the amortization period? ")
years = int(years)

# Calculations
#MonthlyRate = rate / 12
#AnswerMonthlyRate = int(rate)
NumberofPayments = years * 12

#need to figure out calculation for monthly mortgage payments M = L * ((I * ((1+I) ** n)) / ((1+I) ** n - 1))

MonthlyPayments = mortgage * ((rate * ((1+rate) ** NumberofPayments)) / ((1+rate) ** NumberofPayments - 1))


# Answers
print(MonthlyPayments)





