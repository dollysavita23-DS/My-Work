# Calculator using(if and else)


print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

a = int(input("Enter the Number : "))
b = int(input("Enter the Number : "))
Ch = int(input("Enter the Choice : "))

if(Ch == 1):
    print("Addition : ",a+b)
elif(Ch == 2):
    print("Subtraction : ",a-b)
elif(Ch == 3):
    print("Multiplication : ",a*b)
elif(Ch == 4):
    print("Division : ",a/b)
