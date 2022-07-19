import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:

	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
		self.value = values[rank]

	def __str__(self):
		return self.rank + " of " + self.suit

class Deck:
    
    def __init__(self):
        self.cards = [] 
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit,rank))
                
    def shuffle(self):
        random.shuffle(self.cards)
        
    def deal(self):
        return self.cards.pop()        

class Player:
    
    def __init__(self):
        self.hand = []
        self.chips = 20
        self.bet = 0 

    def hit(self):
    	self.hand.append(deck.deal())

    def hit_two(self):
    	self.hand.append(deck.deal())
    	self.hand.append(deck.deal())

    def ask_bet(self):
    	print(f"\nYou have {self.chips} chips remaining.\n")
    	while True:
    		choice = input("How many chips would you like to bet? ")
    		if choice.isdigit():
    			if int(choice) <= self.chips:
    				break
    			else:
    				print("You don't have that many chips!")
    		else:
    			print("Not a number!")
    	bet = int(choice)
    	self.chips = self.chips - bet 
    	self.bet = self.bet + bet   	

    def ask_hit(self):
    	while True:
    		choice = input("\nWould you like to hit? Enter 1 for yes or 2 for no. ")
    		if choice in ['1','2']:
    			break
    	if choice == '1':
    		return True
    	else:
    		return False

    def show_cards(self):
    	print("\nYour current cards are:\n")
    	for card in self.hand:
    		print(card)

class Dealer:

	def __init__(self):
		self.hand = []

	def hit(self):
		self.hand.append(deck.deal())

	def hit_two(self):
		self.hand.append(deck.deal())
		self.hand.append(deck.deal())

	def show_card(self):
		print("\nThe dealer's first card is:\n")
		print(self.hand[0])

	def show_cards(self):
		print("\nThe dealer's cards are:\n")
		for card in self.hand:
			print(card)

def total(hand):

	total = 0
	high_aces = 0

	for card in hand:

		total = total + card.value
		if card.rank == "Ace":
			high_aces = high_aces + 1

	while total > 21 and high_aces > 0:
		total = total - 10
		high_aces = high_aces - 1

	return total

def play_again():

	while True:
		choice = input("\nWould you like to play again? Enter 1 for yes or 2 for no. ")
		if choice in ['1','2']:
			break
	if choice == '1':
		player.hand = []
		dealer.hand = []
		player.bet = 0
		return True
	else:
		return False

# GAME SETUP

player = Player()
dealer = Dealer()
game_on = True

#GAME LOGIC

while game_on:

	deck = Deck()
	deck.shuffle()
	player.ask_bet()
	player.hit_two()
	dealer.hit_two()
	player.show_cards()
	dealer.show_card()
	player_turn = player.ask_hit()

	while player_turn:

		player.hit()
		player.show_cards()

		if total(player.hand) > 21:
			print("\nBust!")
			game_on = play_again()
			break

		player_turn = player.ask_hit()

	while not player_turn:

		if total(dealer.hand) > 21:

			dealer.show_cards()
			print("\nDealer busts. You win!")
			player.chips = player.chips + (player.bet * 2)
			game_on = play_again()
			break

		elif total(dealer.hand) > total(player.hand):

			dealer.show_cards()
			print("\nDealer wins.")
			game_on = play_again()
			break

		elif total(dealer.hand) >= 17:

			if total(dealer.hand) == total(player.hand):

				dealer.show_cards()
				print("It is a tie!")
				player.chips = player.chips + player.bet
				game_on = play_again()
				break

			else:

				dealer.show_cards()
				print("\nYour cards are higher. You win!")
				player.chips = player.chips + (player.bet * 2)
				game_on = play_again()
				break

		else:
			
			dealer.hit()

	if player.chips == 0:
		print("\nYou are out of chips. Game over.")
		game_on = False







