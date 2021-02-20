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
chips = 0


class Hand:
    def __init__(self, cards, aceOneValue, aceElevenValue, hasAce):
        self.cards = cards
        self.aceOneValue = aceOneValue
        self.aceElevenValue = aceElevenValue
        self.hasAce = hasAce

    def add_card(self, card):
        self.cards.append(card)

    def add_card_value(self, cardValue):
        modcardvalue = ((cardValue - 1) % 13) + 1
        modcardvalue = 10 if (modcardvalue > 10) else modcardvalue
        if not self.hasAce and modcardvalue == 1:
            self.aceOneValue += 1
            self.aceElevenValue += 11
            self.hasAce = True
        else:
            self.aceOneValue += modcardvalue
            self.aceElevenValue += modcardvalue

    # def hand_status(self):
    #     if self.aceOneValue > 21:
    #         return 'Bust'
    #     else:
    #         return 'Playable'

    def reset(self):
        self.cards = []
        self.aceOneValue = 0
        self.aceElevenValue = 0
        self.hasAce = False


def new_game(p1, c1):
    global card_deck
    card_deck = deck_of_cards
    # player_hand = []
    # computer_hand = []
    p1.reset()
    c1.reset()


def print_player_cards(cards):
    for card in cards:
        cardstr = ''
        cardval = ((card - 1) % 13) + 1
        cardsuite = int((card - 1) / 13)
        if cardval == 11:
            cardstr = 'Jack'
        elif cardval == 12:
            cardstr = 'Queen'
        elif cardval == 13:
            cardstr = 'King'
        elif cardval == 1:
            cardstr = 'Ace'
        else:
            cardstr = str(cardval)
        cardstr += ' Of '
        if cardsuite == 0:
            cardstr += 'Clubs'
        elif cardsuite == 1:
            cardstr += 'Diamonds'
        elif cardsuite == 2:
            cardstr += 'Spades'
        else:
            cardstr += 'Hearts'
        print(cardstr)
    # print(cards)


def load_game(save_location):
    print('Load')
    # TODO load game from file


def save_game():
    print('Save')
    # TODO save game to file


def player_turn(player):
    card = input('Hit (H) or Stand (S)?')
    if card == 'H':
        print('HIT')
        hit(player)
        return True
    elif card == 'S':
        print('STAND')
        return False


def hit(player):
    cardDrawn = random.randrange(0, len(card_deck), 1)
    cardval = card_deck[cardDrawn]
    player.add_card(cardval)
    del card_deck[cardDrawn]
    player.add_card_value(cardval)


def game_instance(player, computer):
    global chips
    doplay = True



    while doplay:
        if chips == 0:
            print('You currently do not have any chips. Please add some more before you play!')
            break

        playergo = True
        computergo = True
        player1val = 0
        computerval = 0
        status = 0

        if status != 1:
            wager = input('How many tokens would you like to wager?')
            if int(wager) > chips:
                print('You have wagered more than you have chips. You have wagered all your chips instead!')
                wager = chips



        # cardDrawn = random.randrange(0, len(card_deck), 1)
        # cardval = card_deck[cardDrawn]
        # computer.add_card(cardval)
        # del card_deck[cardDrawn]
        # computer.add_card_value(cardval)

        hit(player)
        hit(computer)
        hit(player)

        print('The computer has a face-up card of:')
        print_player_cards(computer.cards)

        print('You have cards of:')
        print_player_cards(player.cards)

        hit(computer)
        computerval = computer.aceElevenValue

        if player.aceElevenValue == 21:
            print('You have a blackjack!')
            playergo = False
            player1val = -2
            if computerval == 21:
                print('The computer also has a blackjack. This hand will be pushed.')
                status = 1
            else:
                print('The computer does not have a blackjack. You win!')
                chips += int((int(wager) * 1.5))

        while playergo:
            playergo = player_turn(player)
            # print(player.aceOneValue)
            # print(player.aceElevenValue)
            print("Your current hand consists of: ")
            print_player_cards(player.cards)
            # curstatus = player.hand_status()
            if player.aceOneValue > 21:
                # print('Bust. Better luck next time!')
                player1val = -1
                break
            else:
                player1val = player.aceElevenValue if player.aceElevenValue < 21 else player.aceOneValue
        # print(player1val)
        if player1val != -1:
            print("The computer's current hand consists of:")
            print_player_cards(computer.cards)
        while player1val >= 0 and computerval < 17:
            hit(computer)
            computerval = computer.aceElevenValue
            print("The computer's current hand consists of:")
            print_player_cards(computer.cards)
            if computerval > 21:
                print('The computer busts! You win!')
                chips += int(wager)
                player1val = -3
                break
        if player1val > -2:
            if player1val > computerval:
                print('You win! Congratulations!')
                chips += int(wager)
            elif player1val == computerval:
                print('You and the computer have the same hand total! This hand will be pushed')
                status = 1
            elif player1val == -1:
                print('You have busted. Better luck next time!')
                chips -= int(wager)
            else:
                print('The computer has the better hand. Better luck next time!')
                chips -= int(wager)
        # print(player1val)
        # print(computerval)

        while status != 1:
            print('You currently have ' + str(chips) + ' chips!')
            goagain = input('Would you like to play again? (Y/N)')
            if goagain == 'Y':
                print('Playing again. Good luck!')
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                new_game(player, computer)
                break
            elif goagain == 'N':
                print('See you next time!')
                doplay = False
                break
            else:
                print('Please input Y or N')



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
    global chips

    print('test')
    player = Hand([], 0, 0, False)
    computer = Hand([], 0, 0, False)
    new_game(player, computer)

    while True:
        app_state = input("Would you like to add chips (A), play blackjack (P), load chip count from previous save (L), or save chip count (S), or quit (Q)?")
        if app_state.upper() == 'A':
            print('You currently have ' + str(chips) + ' chips.')
            chips_add = input('How many chips would you like to add?')
            chips += int(chips_add)
            print('You now have ' + str(chips) + ' chips!')
        if app_state.upper() == 'Q':
            break
        if app_state.upper() == 'P':
            game_instance(player, computer)
        if app_state.upper() == 'S':
            f = open("blackjack_savefile.txt", "w")
            f.write(str(chips))
            f.close()
            print('Saved ' + str(chips) + ' chips into the save!')
        if app_state.upper() == 'L':
            f = open("blackjack_savefile.txt", "r")
            chips = int(f.read())
            print('Your chip count has been loaded from the previous save. You currently have ' + str(chips) + ' chips')
            # print(f.read())
            f.close()
    # print(hand_total([26, 14]))


if __name__ == "__main__":
    main()
