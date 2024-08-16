print ("Loan Interest Calculator")
# 5% APR
print()
principle = int(input("Enter your loan amount: ")) 
rate = float(input("Enter your loan interest rate:"))
x = principle
# Default number of years is 10
#loan calculation
print()
for i in range(10):
  x += (x*rate/100)


print ("Your loan amount after 10 years is", round(x,2))
extra = x - principle 
print ("You paid", round(extra,2), "in interest!")