print("Welcome to the tip calculator!")
totalBill = float(input("What was the totalBill? "))
tipPercentage = int(input("How much tip would you like to give? 10, 12, 15 ? "))
splitPerson = int(input("How many persons to split the bill? "))
totalBillWithTip = (totalBill * tipPercentage / 100) + totalBill
# finalBillPerPerson = round(totalBillWithTip / splitPerson, 2)
finalBillPerPerson = "{:.2f}".format(totalBillWithTip / splitPerson)
print(f"Each person should pay: ₹{finalBillPerPerson}")
