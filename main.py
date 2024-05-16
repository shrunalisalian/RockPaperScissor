import random 
import math 

# define a function play that takes input from the user and computer. Then using if else statements define the 
# states of the game : WIN, LOSS & TIE 

def play():
        while True:
            user = input(" Please enter your input for the game: Rock (r), Paper (p) or Scissor(s) \n ").lower()
            if user in ['r', 'p', 's']:
                break
            else:
                print("Invalid input. Please try again.\n ")

        computer = random.choice(['r', 'p', 's'])
        
        # TIE condition
        if user == computer:
            return (0, user, computer)
        
        # Winning condition
        # r > s, s > p , p > r
        elif (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
            return (1, user, computer)
        
        else:
            return (-1, user, computer)

# Part 2: writing a function that will allow us to play best out of n games 
def play_best_of(n):
    """ 
    Play against computer until someone wins best out of n games 
    to win, you must win ceil (n/2) games (2/3), (4/7), (5/8)
    """
    player_wins = 0 
    computer_wins = 0 
    wins_necessary = math.ceil(n/2)
    while player_wins < wins_necessary and computer_wins < wins_necessary:
        result, user, computer = play()
        if result == 0:
            print(" You and the computer have both chosen {}. It's a tie \n ". format(user))
        elif result ==1:
            player_wins +=1 
            print("You have chosen {}. The computer has chosen {}. You win! \n ".format(user,computer))
        else:
            computer_wins += 1
            print("You have chosen {}. The computer has chosen {}. You lost. \n ".format(user, computer))

    if player_wins > computer_wins:
        print("Hurray! You won best out of {} games".format(n))
    else:
        print(" The computer has won best out of {} games".format(n))


if __name__ == "__main__":
    n = int(input(" Enter number of games you want to play"))
    play_best_of(n)
    

