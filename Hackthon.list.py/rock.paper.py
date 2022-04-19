# In normal rock paper and scissor game
print("press",0,"for rock")
print("press",1,"for paper")
print("press",2,"for scissor")
player_input=int(input("enter the number from the given option above:"))
items=["rock","paper","scissor"]
import random
computer_input=random.randrange(0,2)
print("selected by the player :",items[player_input])
print("selected by the computer :",items[computer_input])
if player_input==0 and computer_input==1:
    print("computer should be the winner")
elif player_input==1 and computer_input==2:
    print("computer should be the winner")
elif player_input==2 and computer_input==0:
    print("computer should be the winner")
elif player_input==1 and computer_input==0:
    print("player should be the winner")
elif player_input==2 and computer_input==1:
    print("player should be the winner")
elif player_input==0 and computer_input==2:
    print("player should be the winner")
else:
    print("both are should be the winners")