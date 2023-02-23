import random

name=input("Enter Your Name:")
print()
print("Hello,",name," Welcome to Rock, Paper and Scissor's official game!")
print()
print("These are some Rule's of the Game")
print("1. Rock wins from Scissor!")
print("2. Paper wins from Rock!")
print("3. Scissor wins from paper!")
print()
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("To play this game use Number's: 1 2 and 3")
print("1 = Rocks")
print("2 = Paper")
print("3 = Scissor ")
print()
game=int(input("To play this game enter a Number:"))
if game==1:
    print("You Chose Rock:")
    print(rock)
elif game==2:
    print("You Chose Paper:")
    print(paper)
elif game==3:
    print("You Chose Scissor:")
    print(scissors)
else:
    print("Choose between 1 to 3.")

comp=random.randint(1,3)
if comp==1:
    print("Computer Chose Rock")
    print(rock)
elif comp==2:
    print("Computer Chose Paper")
    print(paper)
elif comp==3:
    print("Computer Chose Scissor")
    print(scissors)

if comp==game:
    print("It's a Draw",name,"!")
elif comp==1 and game==3:
    print("You lost",name,"!")
elif comp==2 and game==1:
    print("You lost",name,"!")
elif comp==3 and game==2:
    print("You lost",name,"!")
elif game==1 and comp==3:
    print("You won",name,"!")
elif game==1 and comp==2:
    print("You won",name,"!")
elif game==3 and comp==2:
    print("You won",name,"!")
elif game==2 and comp==3:
    print("You won",name,"!")