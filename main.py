#This is the famous blackjack game built using simple python code:

import random
from art import logo

#this code helps pick 2 random cards from the cards list:

user = []
computer = []
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_over = False
for i in range(0, 2):
    user.append(random.choice(cards))
    computer.append(random.choice(cards))

#this code is to swap the ace card with 1 if the total sum of the cards is 21:

def change_ace_card(item):
    if sum(item) > 21:
        if 11 in item[2:]:
            item[item.index(11)] = 1

# This shows the user and computer lists at the end of the game:
def end_game():
    print(f" your final hand {user}, final score: {sum(user)}")
    print(f" computer's final hand {computer}, final score: {sum(computer)}")

# This program checks who wins the game:

def play_game(item):
    global game_over
    if sum(item) > 21:
        game_over = True
        end_game()
        if item == user:
            print("You went over! you lose!")
        elif item == computer:
            print("Computer went over! you win!")
    if sum(item) == 21:
        game_over = True
        end_game()
        if item == user:
            print("You have blackjack! you won!")
        elif item == computer:
            print("Computer has blackjack! you lose!")

#This is the start of the game:

#It shows the initial user cards and the computer's first first hand:

def black_jack():
    print(logo)
    print(f" you current cards {user}, current score: {sum(user)}")
    print(f" computer's first card {computer[0]}")
    game_over = False


game = input(" Press 'y' to play blackjack 'n' to quit: ")

if game == 'y':
    black_jack()
else:
    print('goodbye')


#If user already has 21 then its a blackjack!

if sum(user) == 21:
    game_over = True
    end_game()
    print("You have blackjack! you win!")
elif sum(computer) == 21:
    game_over = True
    end_game()
    print("Computer has a blackjack! you lose!")

#This prompts the user to either draw cards or pass onto the computer:

while game_over == False:
    continue_user = input(" Press 'y' to draw another card or 'n' to pass over: ")
    if continue_user == 'y':
        user.append(random.choice(cards))
        change_ace_card(user)
        play_game(user)
        if game_over == False:
            print(f" you current cards {user}, current score: {sum(user)}")
            print(f" computer's first card {computer[0]}")

#Pass to computer to draw hands:
    #The computer will draw cards unless it has a sum of 17 or greater:

    elif continue_user == 'n':
        while sum(computer) < 17:
            computer.append(random.choice(cards))
            change_ace_card(computer)
            play_game(computer)
#If the game is still not over then compare the scores of the user and computer:

        if game_over == False:
            if sum(user) > sum(computer):
                game_over = True
                end_game()
                print("You win!")
            elif sum(user) < sum(computer):
                game_over = True
                end_game()
                print("You lose!")
            elif sum(user) == sum(computer):
                game_over = True
                end_game()
                print("Its a draw! ")

