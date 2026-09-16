# Count the note

Amount = int(input("Enter the amount : "))
Note = int(input("Which note do you want(100 0r 200 0r 500) : "))

Note1 = Amount//Note
print("Notes are : ",Note1)
Remaining_Note1 = Amount%Note

print("Remaining Rupees is : ",Remaining_Note1)
