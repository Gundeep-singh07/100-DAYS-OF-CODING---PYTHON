#day3
print("Hello, Welcome to Treasure hunt Game!")
print("$$Your task is to find Treasure$$")
print()
name=input("Enter You name:")
print()
a=input("Do you want to start the game(Yes or No?):\n")
print()
if a=="Yes" or a=="yes":
    print("Yayyy, You are all set To Play!")
else:
    print("Don't You want to find your Treasure?")
print()
direction=input("Which direction You want to go (Left or Right)?")
print()
if direction=='Right' or direction=='right':
    print("Oh no,There is a lake.")
    print()
    lake=input("Boat will be arriving in few minutes... Would you Wait or will you Swim?\n")
    if lake=='swim' or lake=='Swim':
        print("Game over.",name,"!","Reason: There were crocodiles.")
    elif lake=='wait' or 'Wait':
        print("The boat has arrived.")
        print()
        print("You are on island",name,"!")
        print()
        print("Now Let's play a Luck roll.")
        print("Choose any of the following:")
        print("1. Climb Mountain's")
        print("2. Dig the land")
        print("3. Go to forest")
        lr=input("What have you decided to choose:\n")
        print()
        if lr=="Climb Mountain's" or lr=="climb mountain" or lr=="climb mountains" or lr=="Climb Mountains" or lr=="Climb Mountain":
            print("Game over!",name,"Reason: There is nothing in the mountains instead of ice.")
        elif lr=="Dig the land" or lr=="dig the land" or lr=="Dig the Land" or lr=="Dig The Land":
            print("Game over!",name,"Reason: There is nothing except stones in land.")
        elif lr=="Go to forest" or lr=="Go To forest" or lr=="Go To Forest" or lr=="go to forest":
            print("You're to close to treasure.")
            print()
            print("Let's See you deserve this treasure or not by last step of this game!")
            print()
            lastcall=input("What will you choose Gun or treasure?")
            if lastcall=="gun" or 'Gun':
                print("You won the treasure!",name)
            elif lastcall=='treasure' or 'Treasure':
                print("You lost it after being so close!!!",name,"Reason: If you would have chosen gun You could have survive from dangerous Lion.")
                print()
                print("Better luck next time.")
elif direction=='Left' or direction=='left':
    print("Game over.")