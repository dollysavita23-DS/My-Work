# Count no. of vowels

string = input("Enter a string:")
count = 0

for ch in string:
    if ch in "a,e,i,o,u":
        count = count + 1
print("Number of vowels =",count)
