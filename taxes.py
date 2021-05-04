earnings= input("Enter your earnings in pounds : ")
earnings=float(earnings)

taxpercent = 20.0
tax = taxpercent / 100.0

taxed = earnings - earnings*tax

print(F"Assuming a tax of {taxpercent}%, your taxed income")
print(F"is equal to {taxed} pounds")