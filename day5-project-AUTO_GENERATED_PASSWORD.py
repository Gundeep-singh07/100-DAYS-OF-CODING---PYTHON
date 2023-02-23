import random

name=input("Enter you name:")
print()
print("Hello",name,"Welcome to the Auto Generated Password's Official Website!")
print()
alpS=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
spec=['!','@','#','$','%','^','&','*']
number=['1','2','3','4','5','6','7','8','9','0']
a=int(input("How many letter password you want:"))
s=int(input("How many Special characters you want:"))
n=int(input("How many Number's Do you want:"))
password=""
for i in range(1,a+1):
    password=password+random.choice(alpS)
for i in range(1,s+1):
    password=password+random.choice(spec)
for i in range(1,n+1):
    password=password+random.choice(number)
print()
print(name,"Your Password is:",password)