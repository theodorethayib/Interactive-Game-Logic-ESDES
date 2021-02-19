'''
1. Replace this block comment with a useful description of what this file and what your game is

Make the game start by running this file.

2. Python Objectives:
    a. Implement intermediate language features in Python (objects, data structures, read/write to file)
    b. Setup a virtual enviroment and import python packages (pygame)
    c. Experiement with GUI

3. Game Objectives:
    a. Code a standard player vs computer game of your choice
    b. The game has an element of randomness and strategy
    c. The computer has to make decisions only considering the state of information available to them as if they were a player
    d. Example: Blackjack has random shuffle but strategy based on your hand, opponents hand, and revealed cards
    e. Example: Battleship has random selection of piece positions and simple strategy involves knowing which direction to guess after a hit
    f. Example: may use read/write to file as a way to save game and continue later

Author:
'''

import random

deck_of_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]

card_deck = []
player_hand = []
computer_hand = []


class Hand:
    def __init__(self, cards, aceOneValue, aceElevenValue, hasAce):
        self.cards = cards
        self.aceOneValue = aceOneValue
        self.aceElevenValue = aceElevenValue
        self.hasAce = hasAce

    def add_card(self, cardValue):
        modcardvalue = ((cardValue - 1) % 13) + 1
        modcardvalue = 10 if (modcardvalue > 10) else modcardvalue
        if not self.hasAce and modcardvalue == 1:
            self.aceOneValue += 1
            self.aceElevenValue += 11
            self.hasAce = True
        else:
            self.aceOneValue += modcardvalue
            self.aceElevenValue += modcardvalue

    def hand_status(self):
        if self.aceOneValue > 21:
            return 'Bust'
        elif self.aceElevenValue == 21 or self.aceOneValue == 21:
            return 'Blackjack'
        else:
            return 'Playable'


def new_game(player, computer):
    card_deck = deck_of_cards
    # player_hand = []
    # computer_hand = []
    player = Hand([], 0, 0, False)
    computer = Hand([], 0, 0, False)


def load_game(save_location):
    print('Load')
    # TODO load game from file


def save_game():
    print('Save')
    # TODO save game to file


# def player_turn():


def hand_total(hand):
    totalace1 = 0
    totalace11 = 0
    for cards in hand:
        # modCard = cards % 13
        totalace1 += min((cards % 13), 10)
        totalace11 += min((cards % 13), 10)
        totalace11 += (10 if ((cards % 13 == 1)) else 0)
        totalace11 += (10 if ((cards % 13 == 0)) else 0)
        totalace1 += (10 if ((cards % 13 == 0)) else 0)

    return [totalace1, totalace11]


def main():
    print('test')
    player = Hand([], 0, 0, False)
    player.add_card(3)
    print(player.aceOneValue)
    computer = Hand([], 0, 0, False)
    new_game(player, computer)
    print(player.aceOneValue)
    # print(hand_total([26, 14]))


if __name__ == "__main__":
    main()
