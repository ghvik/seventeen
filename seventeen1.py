#!/usr/bin/env python
#
# Place-in Sample Exam 2
# Seventeen
#
# seventeen1.py
########################################################################

# Start the game loop, prompt the human to enter a move
def game_loop(num_marbles=17, winner_msg=""):
    print("\nLet's play the game of Seventeen!")
    while num_marbles > 0:
        # player's move
        player_removed = players_move(num_marbles)
        print("You removed {} marbles.".format(player_removed))
        
        # calculate and print number of marbles remaining
        num_marbles = get_marbles_remaining(num_marbles, player_removed)
        
        # Check if the Computer won, i.e. the human removes the last marble
        if num_marbles == 0:
            winner_msg = "Computer wins!"
            break
            
        # computer's move
        computer_removed = computers_move(num_marbles, player_removed)
        print("Computer removed {} marbles.".format(computer_removed))
        
        # calculate and print number of marbles remaining
        num_marbles = get_marbles_remaining(num_marbles, computer_removed)
        
        # Check if the human won, i.e. computer removes the last marble
        if num_marbles == 0:
            winner_msg = "You win!"
            break
    # find winner and print to terminal
    print("\nThere are no marbles left. {}".format(winner_msg))

# The human player's move
def players_move(num_marbles):
    """Prompts the player to pick a move and then returns the number
    of marbles removed
    
    num_marbles -- the number of marbles before the player chooses
        a move
    """
    marbles_left = "Number of marbles left in jar: {}".format(num_marbles)
    print(marbles_left)
    removed = input("\nYour turn: How many marbles will you remove (1-3)? ")
    removed = validate_input(removed, num_marbles)
    return removed

# Validate the human's input
def validate_input(remove_marbles, num_marbles):
    """Validates if the number of marbles to be removed is an integer
    Or if it's a string, return invalid input error msg. Also 
    validates if number entered is greater than 3 or less than 1
    
    Paramter:
    remove_marbles -- the number of marbles to remove as entered by the
        user
    num_marbles -- the number of marbles before the player's move
    """
    try:
        remove_marbles = int(remove_marbles)
    except ValueError:
        print("Sorry, that is not a valid option. Try again!")
        # print("Please enter non-word numerals.")
        remove_marbles = players_move(num_marbles)     
    else:
        # Check out of bounds conditions
        if num_marbles < remove_marbles:
           print("Sorry, that is not a valid option. Try again!")
           # print("There are only {} marbles left in the jar.".format(num_marbles))
           remove_marbles = players_move(num_marbles)
           
        if remove_marbles < 1 or remove_marbles > 3:
            print("Sorry, that is not a valid option. Try again!")
            remove_marbles = players_move(num_marbles)
    finally:
        return remove_marbles

# Proceed with the computer's strategy
def computers_move(num_marbles, human_removed):
    """Returns the number of marbles the computer removes based on
    some strategy. Currently the computer will employ the simple
    strategy of matching the same move as the human player
    
    Parameter:
    num_marbles -- the number of marbles before the computer makes
        its move
    human_removed -- the number of marbles that the human removed
    """
    print("Number of marbles left in jar: {} ".format(num_marbles))
    print("\nComputer's turn...")
    if num_marbles < human_removed:
        return num_marbles
    else:
        return human_removed

# Gets the number of marbles remaining at the end of the turn
def get_marbles_remaining(previous_count, marbles_removed):
    """Get the current number of marbles remaining in the jar
    at the end of each turn
    
    Parameters:
    previous_count -- the previous count of marbles in the jar
    marbles_removed -- the number of marbles removed in a turn
    """
    remaining = previous_count - marbles_removed
    return remaining

def main():
    game_loop()

if __name__ == "__main__":
    main()