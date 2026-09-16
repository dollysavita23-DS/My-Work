# Compound Interest

p = int(input("Enter the principle amount : "))
r = int(input("Enter the Rate of interest : "))
t = int(input("Enter the Time in Years : "))
n = int(input("Enter the no. of times the interest is compounded : "))

Amount = p*(1+r/n)**n*t

print("Compound Interest is : ",Amount)
