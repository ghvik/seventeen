#!/usr/bin/env python
#
# Place-in Sample Exam 2
# Seventeen
#
# seventeen2.py
########################################################################

# Model
def get_games(input_file):
    """Returns a list of games based on an input file
    
    input_file -- the text file used to determine the player's
        sequence of moves
    """
    #print("Number of marbles left in jar: {}".format(num_marbles))
    with open(input_file, "r") as fin:
        all_games = fin.readlines()
    return all_games

# View
def display_games(game_list, num_marbles=17):
    """Display a list of games based on an input file which has a
    list of a player's moves
    
    game_list -- the list that contains all the moves for player 1
        does in 10 different games
    num_marbles -- the number of marbles at the start of the game
    """
    for game, turns in enumerate(game_list, 1):
        turns = turns.strip()
        turn_list = turns.split(',')
        play_sequence, winner = get_sequence_and_winner(num_marbles, turn_list)
        print("Game #{}. Play sequence: {}. Winner: {}"
            .format(game, play_sequence, winner))

# Controller
def get_sequence_and_winner(remaining, player1_turns):
    """This is the game loop for each game in the file. It assumes
    that there are enough player1 moves in the file for the game to always
    finish
    
    Parameters:
    remaining -- the number of marbles remaining in the jar at the start
        of each turn
    player1_turns -- a list of player1's turns in each of the games
    """
    sequence = ""
    for p1_turn in player1_turns:
        p1_turn = int(p1_turn)
        if remaining < p1_turn:
            p1_turn = remaining
        remaining = get_marbles_remaining(remaining, p1_turn)
        if remaining == 0:
            sequence += "{}".format(p1_turn)
            winner = "P2"
            break
        else:
            sequence += "{}-".format(p1_turn)
        computer_removed = computers_move(p1_turn)
        if remaining < computer_removed:
            computer_removed = remaining
        remaining = get_marbles_remaining(remaining, computer_removed)
        if remaining == 0:
            sequence += "{}".format(computer_removed)
            winner = "P1"
            break
        else:
            sequence += "{}-".format(computer_removed)
            
    return sequence, winner

# The computer's strategy
def computers_move(human_removed):
    """Returns the number of marbles the computer removes based on
    some strategy. Currently the computer will employ the simple
    strategy of matching the same move as the human player
    
    Parameter:
    num_marbles -- the number of marbles before the computer makes
        its move
    human_removed -- the number of marbles that the human removed
    """
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
    game_list = get_games("i206_placein_input_0.txt")
    display_games(game_list)

if __name__ == "__main__":
    main()