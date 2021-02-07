income = int(input("Please enter your taxable income: $"))


tax = 0.0

if income <= 9875:
	tax = income * .10
elif income <= 40125:
	tax = 987.50 + .12 * (income - 9875)
elif income <= 85525:
	tax = 4617.50 + .22 * (income - 40125)
elif income <= 163300:
	tax = 14605.50 + .24 * (income - 85525)
elif income <= 207350:
	tax = 33271.50 + .32 * (income - 163300)
elif income <= 518400:
	tax = 47367.5 + .35 * (income - 207350)
else:
	tax = 156235 + .37 * (income - 518400)

remainder = income - tax

print("You pay ${tax}".format(tax = tax),"in income tax\n")

print("You have ${rem}".format(rem =remainder), "left\n")