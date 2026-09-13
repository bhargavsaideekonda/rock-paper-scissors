import random
list_a = ["rock", "paper", "scissors"]
# scoring: a win pays 1, a draw pays 1 to each player
you = 0
me = 0
for each_round in range(5):
    print(f"Round {each_round + 1} of 5")
    user = input("Your choice (rock/paper/scissors): ")
    computer_choice=random.choice(list_a)
    print(f"You chose {user}, I chose {computer_choice}.")
    if user == computer_choice:
        print("Draw.")
        you = you + 1
        me = me + 1
        print(f"Score -  You: {you}   Me: {me}")
    elif (user == list_a[0] and computer_choice == list_a[2]) or (user == list_a[1] and computer_choice == list_a[0]) or (user == list_a[2] and computer_choice == list_a[1]):
        print("You win this round.")
        you = you + 1
        print(f"Score -  You: {you}   Me: {me}")
    else:
        print("I win this round.")
        me = me + 1
        print(f"Score -  You: {you}   Me: {me}")
print(f"FINAL SCORE - You: {you}  Me: {me}")
if you > me:
    print("You win this match.")
elif you == me:
    print("Draw.")
else:
    print("I win this match.")
    
    