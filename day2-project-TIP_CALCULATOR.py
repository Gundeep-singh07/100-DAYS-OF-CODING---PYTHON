#This is a Tip calculator
print("Hello, Welcome to Tip calculator!")
print()
bill=int(input("What is Your Total Bill:\n"))
tip=int(input("Enter the Amount of Tip You Want to Give? 10%,12% or 15%:\n"))
print()
t=tip/bill*100
print("The tip You are going to pay:",tip/bill*100)
print()
totalbill=bill+t
print("Total bill is:",totalbill)
print()
split=int(input("In how many people do you want to split the bill:\n"))
print("You all have to pay:",totalbill/split)