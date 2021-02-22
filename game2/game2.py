'''
1. Blackjack Game

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

Author: Theodore Thayib
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

def player_turn(player):
    card = input('\nHit (H) or Stand (S)?')
    if card.upper() == 'H':
        hit(player)
        return True
    elif card.upper() == 'S':
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
    status = 0



    while doplay:
        if chips == 0:
            print('You currently do not have any chips. Please add some more before you play!\n')
            break

        playergo = True
        computergo = True
        player1val = 0
        computerval = 0


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

        print('\nThe computer has a face-up card of:')
        print_player_cards(computer.cards)

        print('\nYou have cards of:')
        print_player_cards(player.cards)

        hit(computer)
        computerval = computer.aceElevenValue
        # print('\n')

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
                status = 0

        while playergo:
            playergo = player_turn(player)
            # print(player.aceOneValue)
            # print(player.aceElevenValue)
            print("\nYour current hand consists of: ")
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
            print("\nThe computer's current hand consists of:")
            print_player_cards(computer.cards)
        while player1val >= 0 and computerval < 17:
            hit(computer)
            computerval = computer.aceElevenValue
            print("\nThe computer's current hand consists of:")
            print_player_cards(computer.cards)
            if computerval > 21:
                print('\nThe computer busts! You win!')
                chips += int(wager)
                player1val = -3
                status = 0
                break
        if player1val > -2:
            if player1val > computerval:
                print('\nYou win! Congratulations!')
                chips += int(wager)
                status = 0
            elif player1val == computerval:
                print('\nYou and the computer have the same hand total! This hand will be pushed')
                status = 1
            elif player1val == -1:
                print('\nYou have busted. Better luck next time!')
                chips -= int(wager)
                status = 0
            else:
                print('\nThe computer has the better hand. Better luck next time!')
                chips -= int(wager)
                status = 0
        # print(player1val)
        # print(computerval)

        while status != 1:
            print('\nYou currently have ' + str(chips) + ' chips!\n')
            goagain = input('Would you like to play again? (Y/N)')
            if goagain.upper() == 'Y':
                print('Playing again. Good luck!')
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                new_game(player, computer)
                break
            elif goagain.upper() == 'N':
                print('See you next time!\n')
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

    player = Hand([], 0, 0, False)
    computer = Hand([], 0, 0, False)
    new_game(player, computer)

    while True:
        app_state = input("Would you like to add chips (A), play blackjack (P), load chip count from previous save (L), or save chip count (S), or quit (Q)?")
        if app_state.upper() == 'A':
            print('You currently have ' + str(chips) + ' chips.')
            chips_add = input('How many chips would you like to add?')
            chips += int(chips_add)
            print('\nYou now have ' + str(chips) + ' chips!\n')
        if app_state.upper() == 'Q':
            print('\nSee you next time!')
            break
        if app_state.upper() == 'P':
            game_instance(player, computer)
        if app_state.upper() == 'S':
            f = open("blackjack_savefile.txt", "w")
            f.write(str(chips))
            f.close()
            print('\nSaved ' + str(chips) + ' chips into the save!\n')
        if app_state.upper() == 'L':
            f = open("blackjack_savefile.txt", "r")
            chips = int(f.read())
            print('\nYour chip count has been loaded from the previous save. You currently have ' + str(chips) + ' chips\n')
            # print(f.read())
            f.close()
    # print(hand_total([26, 14]))


if __name__ == "__main__":
    main()
