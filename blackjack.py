from deck import Deck
from hand import DealerHand, PlayerHand
from card import Card

from numpy.random import randint, seed
seed(20)

class Blackjack:
    """
    Game of blackjack!

    # Removes the game summaries from the previous doctest run
    >>> from os import remove, listdir
    >>> for f in listdir("game_summaries"):
    ...    remove("game_summaries/" + f)

    #######################################
    ### Doctests for calculate_score() ####
    #######################################
    >>> card_1 = Card("A", "diamonds")
    >>> card_2 = Card("J", "spades")
    >>> hand_1 = PlayerHand()
    >>> Blackjack.calculate_score(hand_1)
    0
    >>> hand_1.add_card(card_1)
    >>> Blackjack.calculate_score(hand_1) # (Ace)
    11
    >>> hand_1.add_card(card_2)
    >>> Blackjack.calculate_score(hand_1) # (Ace, Jack)
    21

    >>> card_3 = Card("A", "spades")
    >>> hand_2 = PlayerHand()
    >>> hand_2.add_card(card_1, card_3)
    >>> Blackjack.calculate_score(hand_2) # (Ace, Ace)
    12
    >>> hand_2.add_card(card_2)
    >>> Blackjack.calculate_score(hand_2) # (Ace, Ace, Jack)
    12

    >>> hand_3 = PlayerHand()
    >>> card_4 = Card(2, "spades")
    >>> card_5 = Card(4, "spades")
    >>> hand_3.add_card(card_4, card_5)
    >>> Blackjack.calculate_score(hand_3)
    6
    
    # empty check A's check 21 check below 21 check
    
    >>> h = PlayerHand()
    >>> g = PlayerHand()
    >>> d = DealerHand()
    >>> h.add_card(Card("A", "diamonds"), Card('J', "spades"))
    >>> Blackjack.calculate_score(h)
    21
    >>> g.add_card(Card('K', 'spades'), Card('K', 'clubs'), \
Card('A', "spades"), Card('A', 'hearts'))
    >>> Blackjack.calculate_score(g)
    22
    >>> d.add_card(Card(7, 'clubs'), Card(8, 'clubs'), Card(2, 'clubs'))
    >>> Blackjack.calculate_score(d)
    17
    >>> l = PlayerHand()
    >>> l.add_card(Card('A', 'hearts'), Card('A', 'diamonds'), \
Card('A', 'spades'))
    >>> Blackjack.calculate_score(l)
    13
    >>> f = PlayerHand()
    >>> f.add_card(Card('A', 'hearts'), Card('A', 'diamonds'), \
Card('A', 'spades'), Card('A', 'clubs'))
    >>> Blackjack.calculate_score(f)
    14
    
    >>> Blackjack.calculate_score(5)
    Traceback (most recent call last):
    ...
    AssertionError
    
    #######################################
    ### Doctests for determine_winner() ###
    #######################################
    >>> blackjack = Blackjack(10)
    >>> blackjack.determine_winner(10, 12)
    -1
    >>> blackjack.determine_winner(21, 21)
    0
    >>> blackjack.determine_winner(22, 23)
    0
    >>> blackjack.determine_winner(12, 2)
    1
    >>> blackjack.determine_winner(22, 2)
    -1
    >>> blackjack.determine_winner(2, 22)
    1
    >>> print(blackjack.get_log())
    Player lost with a score of 10. Dealer won with a score of 12.
    Player and Dealer tie.
    Player and Dealer tie.
    Player won with a score of 12. Dealer lost with a score of 2.
    Player lost with a score of 22. Dealer won with a score of 2.
    Player won with a score of 2. Dealer lost with a score of 22.
    <BLANKLINE>  
    >>> blackjack.reset_log()

    ##################################
    ### Doctests for play_round() ####
    ##################################
    >>> blackjack_2 = Blackjack(10)
    >>> blackjack_2.play_round(1, 15)
    >>> print(blackjack_2.get_log())
    Round 1 of Blackjack!
    wallet: 10
    bet: 5
    Player Cards: (10, clubs) (A, clubs)
    Dealer Cards: (Q, clubs) (?, ?)
    Dealer Cards Revealed: (7, diamonds) (Q, clubs)
    Player won with a score of 21. Dealer lost with a score of 17.
    <BLANKLINE>
    >>> blackjack_2.reset_log()
   
    >>> blackjack_2.play_round(3, 21)
    >>> print(blackjack_2.get_log())
    Round 2 of Blackjack!
    wallet: 15
    bet: 5
    Player Cards: (4, clubs) (7, clubs)
    Dealer Cards: (A, hearts) (?, ?)
    Player pulled a (J, hearts)
    Dealer Cards Revealed: (5, clubs) (A, hearts)
    Dealer pulled a (6, clubs)
    Dealer pulled a (2, clubs)
    Dealer pulled a (8, clubs)
    Player won with a score of 21. Dealer lost with a score of 22.
    Round 3 of Blackjack!
    wallet: 20
    bet: 10
    Player Cards: (6, hearts) (9, diamonds)
    Dealer Cards: (K, hearts) (?, ?)
    Player pulled a (Q, hearts)
    Dealer Cards Revealed: (J, diamonds) (K, hearts)
    Player lost with a score of 25. Dealer won with a score of 20.
    Round 4 of Blackjack!
    wallet: 10
    bet: 5
    Player Cards: (5, diamonds) (10, diamonds)
    Dealer Cards: (2, diamonds) (?, ?)
    Player pulled a (3, diamonds)
    Player pulled a (7, spades)
    Dealer Cards Revealed: (2, diamonds) (2, hearts)
    Dealer pulled a (K, spades)
    Dealer pulled a (3, spades)
    Player lost with a score of 25. Dealer won with a score of 17.
    <BLANKLINE>
    
    >>> with open("game_summaries/game_summary2.txt", encoding = 'utf-8') as f:
    ...     lines = f.readlines()
    ...     print("".join(lines[10:26]))
    Dealer Hand:
    ____
    |7  |
    | ♦ |
    |__7|
    ____
    |Q  |
    | ♣ |
    |__Q|
    Winner of ROUND 1: Player
    <BLANKLINE>
    ROUND 2:
    Player Hand:
    ____
    |4  |
    | ♣ |
    <BLANKLINE>

    >>> blackjack_3 = Blackjack(5)
    >>> blackjack_3.play_round(5, 21)
    >>> print(blackjack_3.get_log())
    Round 1 of Blackjack!
    wallet: 5
    bet: 5
    Player Cards: (2, clubs) (2, hearts)
    Dealer Cards: (2, diamonds) (?, ?)
    Player pulled a (3, clubs)
    Player pulled a (3, diamonds)
    Player pulled a (3, hearts)
    Player pulled a (3, spades)
    Player pulled a (4, clubs)
    Player pulled a (4, diamonds)
    Dealer Cards Revealed: (2, diamonds) (2, spades)
    Dealer pulled a (4, hearts)
    Dealer pulled a (4, spades)
    Dealer pulled a (5, clubs)
    Player lost with a score of 24. Dealer won with a score of 17.
    Wallet amount $0 is less than bet amount $5.

    >>> blackjack_4 = Blackjack(500)
    >>> blackjack_4.play_round(13, 21) # At least 52 cards will be dealt
    >>> blackjack_4.reset_log()
    >>> blackjack_4.play_round(1, 17)
    >>> print(blackjack_4.get_log())
    Not enough cards for a game.
    
    # >>> blackjack_5 = Blackjack(50)
    # >>> blackjack_5.play_round(10, 18)
    # >>> print(blackjack_5.get_log())
    # 
    # >>> with open("game_summaries/game_summary5.txt", encoding = 'utf-8') as f:
    # ...     lines = f.readlines()
    # ...     print("".join(lines))
    """
    # Class Attribute(s)
    num_class_instances = 0
    
    def __init__(self, wallet):
        # Initializes instance attributes
        # auto-increment as needed
        assert isinstance(wallet, (int, float))
        self.num_games = 0
        self.Deck = Deck()
        self.wallet = wallet
        self.log = ""
        Blackjack.num_class_instances += 1
        self.bet = 0
    
    def play_round(self, num_rounds, stand_threshold):
        """
        Plays `num_rounds` Blackjack rounds.

        Parameters:
            num_rounds (int): Number of rounds to play.
            stand_threshold (int): Score threshold for when the player
            will stand (ie player stands if they have a score >= 
            this threshold)
        """
        assert isinstance(num_rounds, int) and not isinstance(num_rounds, bool)
        assert isinstance(stand_threshold, int) and not isinstance(stand_threshold, bool)
        assert 0 <= stand_threshold <= 21
        self.bet = 5
        for round in range(num_rounds):
            self.num_games += 1
            self.playerhand = PlayerHand()
            self.dealerhand = DealerHand()
            if self.bet < 5:
                self.bet = 5
            if len(self.Deck.get_cards()) < 4:
                self.log += 'Not enough cards for a game.'
                return
            if self.wallet < self.bet:
                self.log += f"Wallet amount ${self.wallet} is less than bet amount ${self.bet}."
                return
            self.log += f'Round {self.num_games} of Blackjack!\nwallet: {self.wallet}\nbet: {self.bet}\n'
            mong = randint(6)
            overhand = randint(6)
            self.Deck.shuffle(modified_overhand=overhand, mongean=mong)
            for d in range(2):
                self.Deck.deal_hand(self.playerhand)
                self.Deck.deal_hand(self.dealerhand)
            
            self.log += f"Player Cards: {repr(self.playerhand.get_cards()[0])} {repr(self.playerhand.get_cards()[1])}\n"
            self.log += f"Dealer Cards: {repr(self.dealerhand.get_cards()[0])} {repr(self.dealerhand.get_cards()[1])}\n"            
            
            self.hit_or_stand(self.playerhand, stand_threshold)
            self.dealerhand.reveal_hand()
            self.log += f"Dealer Cards Revealed: {repr(self.dealerhand.get_cards()[0])} {repr(self.dealerhand.get_cards()[1])}\n"
            self.hit_or_stand(self.dealerhand, 17)
            
            winner = self.determine_winner(Blackjack.calculate_score(self.playerhand), Blackjack.calculate_score(self.dealerhand))
            
            self.wallet += winner*self.bet
            self.bet += winner*5
            self.add_to_file(self.playerhand, self.dealerhand, winner)
        
    def calculate_score(hand):
        """
        Calculates the score of a given hand. 

        Sums up the ranks of each card in a hand. Jacks, Queens, and Kings
        have a value of 10 and Aces have a value of 1 or 11. The value of each
        Ace card is dependent on which value would bring the score closer
        (but not over) 21. 

        Parameters:
            hand: The hand to calculate the score of.
        Returns:
            The best score as an integer value.
        """
        assert isinstance(hand, (DealerHand, PlayerHand))
        score = 0
        ranks = [card.get_rank() for card in hand.get_cards()]
        score += sum([10 if rank == 'K' or rank == 'J' or rank == 'Q' \
        else rank if rank != 'A' else 0 for rank in ranks])
        Aces = ranks.count('A')
        if Aces == 1:
            if score + 11 <= 21:
                score += 11
            else:
                score += 1
        elif Aces == 2:
            if score + 12 <= 21:
                score += 12
            else:
                score += 2
        elif Aces == 3:
            if score + 13 <= 21:
                score += 13
            else:
                score += 3
        elif Aces == 4:
            if score + 14 <= 21:
                score += 14
            else:
                score += 4
        return score

    def determine_winner(self, player_score, dealer_score):
        """
        Determine whether the Blackjack round ended with a tie, dealer winning, 
        or player winning. Update the log to include the winner and
        their scores before returning.

        Returns:
            1 if the player won, 0 if it is a tie, and -1 if the dealer won
        """
        if player_score == dealer_score or (dealer_score > 21 and player_score > 21):
            self.log += 'Player and Dealer tie.\n'
            return 0
        elif (player_score > dealer_score or dealer_score > 21) and player_score <= 21:
            self.log += f'Player won with a score of {player_score}. Dealer lost with a score of {dealer_score}.\n'
            return 1
        elif dealer_score > player_score or player_score > 21:
            self.log += f'Player lost with a score of {player_score}. Dealer won with a score of {dealer_score}.\n'
            return -1

    def hit_or_stand(self, hand, stand_threshold):
        """
        Deals cards to hand until the hand score has reached or surpassed
        the `stand_threshold`. Updates the log everytime a card is pulled.

        Parameters:
            hand: The hand the deal the cards to depending on its score.
            stand_threshold: Score threshold for when the player
            will stand (ie player stands if they have a score >= 
            this threshold).
        """
        assert isinstance(hand, (PlayerHand, DealerHand))
        if len(self.Deck.get_cards()) == 0:
            return
        if Blackjack.calculate_score(hand) >= stand_threshold:
            return
        
        cards = hand.get_cards()[:]
        
        self.Deck.deal_hand(hand)
        if isinstance(hand, DealerHand):
            player = 'Dealer'
        else:
            player = 'Player'
        
        new_cards = hand.get_cards()[:]
        for card in cards:
            new_cards.remove(card)
        assert len(new_cards) == 1
        new_card = new_cards[0]
        
        self.log += f'{player} pulled a ({new_card.get_rank()}, {new_card.get_suit()})\n'
        return self.hit_or_stand(hand, stand_threshold)

    def get_log(self):
        return self.log
    
    def reset_log(self):
        self.log = ""
        return
        
        
    def add_to_file(self, player_hand, dealer_hand, result):
        """
        Writes the summary and outcome of a round of Blackjack to the 
        corresponding .txt file.
        """
        if result == 1:
            winner = 'Player'
        elif result == -1:
            winner = 'Dealer'
        elif result == 0:
            winner = 'Tied'
        fn = f"./game_summaries/game_summary{Blackjack.num_class_instances}.txt"
        
        with open(fn, 'a', encoding = "utf-8") as f:
            f.write('ROUND ' + str(self.num_games) + ':\n' + 'Player Hand:\n' \
            + str(player_hand) + '\n' +  'Dealer Hand:\n' + str(dealer_hand) \
            + '\n' + 'Winner of ROUND ' + str(self.num_games) + ': ' + winner + '\n\n')
