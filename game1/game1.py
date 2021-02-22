'''
1. tic tac toe pog

Make the game start by running this file.

2. Python Objectives:
    a. Implement basic language features of Python (variables, ifs, loops, functions)
    b. Document your code with proper conventions
    c. Experiment with a debugger (a tutorial for the VSCode debugger is in Python workshop setup guide)

3. Game Objectives:
    a. Code a simple player vs computer game of your choice
    b. Winner of the game is decided on a function between the current state of the game and both player inputs
    c. A final winner may be decided after multiple rounds of input
    d. Example: tictactoe winner is decided based on current state of game and the player's input
    e. Tictactoe game board can be stored in a list, and the player input could be verified by making sure input is an open space
    
Author: blub blub blub
'''

import random

game_state = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

def foo(game_state, user_choice, computer_choice):
    ...

def new_game():
    global game_state
    game_state = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

def get_user_input():
    temp = input("TESDF").upper()
    print(temp)

def edit_game_state(xox, loc):
    game_state[int(loc[0])][int(loc[1])] = xox

def computer_move():
    possible_moves = []
    for i in range(len(game_state)):
        for j in range(len(game_state)):
            if game_state[i][j] == " ":
                possible_moves.append(i * 3 + j)
    rand_move = random.randrange(0, len(possible_moves), 1)
    loc_move = [int(possible_moves[rand_move] / 3), int(possible_moves[rand_move] % 3)]
    edit_game_state("O", loc_move)


def show_game_state():
    print(game_state[0][0] + '|' + game_state[0][1] + '|' + game_state[0][2])
    print('------')
    print(game_state[1][0] + '|' + game_state[1][1] + '|' + game_state[1][2])
    print('------')
    print(game_state[2][0] + '|' + game_state[2][1] + '|' + game_state[2][2])

def edit_game_state(xox, loc):
    game_state[int(loc[0])][int(loc[1])] = xox

def get_user_input(xox_input):
    loc_input = get_loc_input()
    edit_game_state(xox_input, loc_input)

def vs_computer_input():
    loc_input = get_loc_input()
    edit_game_state("X", loc_input)

def get_loc_input():
    while True:
        loc_input = []
        while True:
            loc1 = input("Please enter row number between 0-2.")
            if loc1 == "0" or loc1 == "1" or loc1 == "2":
                break
            else:
                print("You did not enter a number between 0-2, try again.")
        loc_input.append(loc1)
        while True:
            loc2 = input("Please enter row number between 0-2.")
            if loc2 == "0" or loc2 == "1" or loc2 == "2":
                break
            else:
                print("You did not enter a number between 0-2, try again.")
        loc_input.append(loc2)
        if game_state[int(loc_input[0])][int(loc_input[1])] == " ":
            break
        else:
            print("That square is occupied. ):<")

    return loc_input

def win_lose():
    if game_state[0][0] == game_state[1][0] and game_state[0][0] == game_state[2][0] and game_state[0][0] != " ":
        if game_state[0][0] == 'X':
            return 1
        return 2
    if game_state[0][1] == game_state[1][1] and game_state[0][1] == game_state[2][1] and game_state[0][1] != " ":
        if game_state[0][1] == 'X':
            return 1
        return 2
    if game_state[0][2] == game_state[1][2] and game_state[0][2] == game_state[2][2] and game_state[0][2] != " ":
        if game_state[0][2] == 'X':
            return 1
        return 2
    if game_state[0][0] == game_state[0][1] and game_state[0][0] == game_state[0][2] and game_state[0][0] != " ":
        if game_state[0][0] == 'X':
            return 1
        return 2
    if game_state[1][0] == game_state[1][1] and game_state[1][0] == game_state[1][2] and game_state[1][0] != " ":
        if game_state[1][0] == 'X':
            return 1
        return 2
    if game_state[2][0] == game_state[2][1] and game_state[2][0] == game_state[2][2] and game_state[2][0] != " ":
        if game_state[2][0] == 'X':
            return 1
        return 2
    if game_state[0][0] == game_state[1][1] and game_state[0][0] == game_state[2][2] and game_state[0][0] != " ":
        if game_state[0][0] == 'X':
            return 1
        return 2
    if game_state[0][2] == game_state[1][1] and game_state[1][1] == game_state[2][0] and game_state[2][0] != " ":
        if game_state[0][0] == 'X':
            return 1
        return 2

    temp = 1
    for i in range(len(game_state)):
        for j in range(len(game_state)):
            if game_state[i][j] == " ":
                temp = 0
    if temp == 1:
        return 3

    return 0

def computer_move():
    possible_moves = []
    for i in range(len(game_state)):
        for j in range(len(game_state)):
            if game_state[i][j] == " ":
                possible_moves.append(i * 3 + j)
    rand_move = random.randrange(0, len(possible_moves), 1)
    loc_move = [int(possible_moves[rand_move] / 3), int(possible_moves[rand_move] % 3)]
    edit_game_state("O", loc_move)

def vs_computer():
    new_game()

    play = 0

    while play == 0:
        vs_computer_input()
        show_game_state()
        play = win_lose()
        print("\n")
        if play == 0:
            computer_move()
            show_game_state()
            play = win_lose()
    if play == 1:
        print("Congratulations! You've won! :D")
    elif play == 2:
        print("You've lost.")
    elif play == 3:
        print("Draw!")


def vs_player():
    new_game()

    play = 0

    while play == 0:
        get_user_input("X")
        show_game_state()
        play = win_lose()
        print("\n")
        if play == 0:
            get_user_input("O")
            show_game_state()
            play = win_lose()
    if play == 1:
        print("Congratulations, Player 1 has won! :D")
    elif play == 2:
        print("Congratulations, Player 2 has won! :D")
    elif play == 3:
        print("Draw!")

def main():
    while True:
        user_input = input("Would you like to play against a computer (C), a player (P), or quit (Q)?").upper()
        if user_input == "C":
            vs_computer()
        elif user_input == "P":
            vs_player()
        elif user_input == "Q":
            print("Bye.")
            break


    # while True:
    #     #TODO: prompt user to make a selection or call a function to retrieve it
    #     #needs validation
    #     user_choice = None
    #
    #     #TODO: select computer's choice or call a function to retrieve it
    #     computer_choice = None
    #
    #     #TODO: decide and display the results
    #     game_result = foo(game_state, user_choice, computer_choice)
    #
    #     #TODO: implement quit or start new game condition
    #     if False:
    #         break

if __name__ == "__main__":
    main()