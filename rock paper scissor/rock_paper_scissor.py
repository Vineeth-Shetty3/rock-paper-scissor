import random

user_wins=0
comp_wins=0

options =["rock", "paper", "scissors"]


while True:
    user_input= input("type Rock/Paper/Scissors or Q to quit:  ").lower()
    if user_input=="q":
        break
    
    if user_input not in options:
        continue
    
    random_numb = random.randint(0, 2)
    #rock-0 paper -1 scissors -2
    computer_pick= options[random_numb]
    print("computer picked ", computer_pick + ".")

    if user_input=="rock" and computer_pick =="scissors":
        print("you win")
        user_wins+=1
    
    elif user_input=="paper" and computer_pick =="rock":
        print("you win")
        user_wins+=1
        
    elif user_input=="scissors" and computer_pick =="paper":
        print("you win")
        user_wins+=1
    
    else:
        print("you lose")
        comp_wins+=1

print("you won ", user_wins ," times.")
print("computer won ", comp_wins, " times.")
print("well done ")


