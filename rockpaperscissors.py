# Import module's random and math #
# You can reach me out via email #
# Enjoy :) #
import random
import math

# Choices #
choices = ["r", "p", "s"]

def play_game():
    # Number of Games #
    num_games = int(input("How Many Games do you want to play?:\n"))
    
    # Store Scores #
    user_wins = 0
    computer_wins = 0
    game_cap = math.ceil(num_games/2) # number of wins a player gets (ex. 3 games, if user scores 2 the game ends) #

    while True:
        user = input("Rock (r), Paper (p), Scissors (s):\n") # User Choice #
        computer = random.choice(choices) # Computer Choice #

        # Tie #
        if user == computer:
            print("It's A Tie!! You picked: {} and the Computer picked: {}\n".format(user, computer))
        
        # User Win #
        elif (user == "r" and computer == "s") or (user == "p" and computer == "r") or (user == "s" and computer == "p"):
            user_wins += 1
            print("You Win!! You picked: {} and the Computer picked: {}\n".format(user, computer))
        
        # Computer Win #
        else:
            computer_wins += 1
            print("The Computer Win!! You picked: {} and the Computer picked: {}\n".format(user, computer))
        
        # If the user reached the game cap the loop ends #
        if user_wins == game_cap:
            print("You Won {} out of {} game\n".format(user_wins, num_games))
            break

        # If the computer reached the game cap the loop ends #
        elif computer_wins == game_cap:
            print("You lose!! The Computer won {} out of {} game\n".format(computer_wins, num_games))
            break

        print("User Score: {} Computer Score: {}\n".format(user_wins, computer_wins)) # prints out the scores #

play_game() # execute #