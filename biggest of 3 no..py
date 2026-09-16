# Find Biggest of the given three no.

num1 = int(input("Enter the Number : "))
num2 = int(input("Enter the Number : "))
num3 = int(input("Enter the Number : "))

if(num1>num2):
    if(num1>num3):
        print("Num1 is Biggest")
    else:
        print("Num3 is Biggest")
else:
    if(num2>num3):
        print("Num2 is Biggest")
    else:
        print("Num3 is Biggest")
        
