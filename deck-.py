from card import Card
from hand import PlayerHand, DealerHand
from shuffle import Shuffle

class Deck:
    """
    Card deck of 52 cards.

    >>> deck = Deck()
    >>> deck.get_cards()[:5]
    [(2, clubs), (2, diamonds), (2, hearts), (2, spades), (3, clubs)]

    >>> deck.shuffle(modified_overhand=2, mongean=3)
    >>> deck.get_cards()[:5]
    [(A, clubs), (Q, clubs), (10, clubs), (7, diamonds), (5, diamonds)]

    >>> hand = PlayerHand()
    >>> deck.deal_hand(hand)
    >>> deck.get_cards()[0]
    (Q, clubs)

    >>> deck = Deck()
    >>> deck.shuffle()
    >>> hand = PlayerHand()
    >>> deck.shuffle(modified_overhand=0, mongean=0)
    >>> deck.deal_hand(hand)
    >>> hand.get_cards()
    [(2, clubs)]
    >>> deck.get_cards()[0]
    (2, diamonds)

    >>> dealer_hand = DealerHand()
    >>> deck.deal_hand(dealer_hand)
    >>> deck.deal_hand(dealer_hand)
    >>> dealer_hand.get_cards()
    [(2, diamonds), (?, ?)]
    """

    # Class Attribute(s)

    def __init__(self):
        """
        Creates a Deck instance containing cards sorted in ascending order.
        """

        suits = ["clubs", "diamonds", "hearts", "spades"]
        ranks = list(range(2, 11)) + ["J", "Q", "K", "A"]

        self.cards = [(Card(r,s)) for r in ranks for s in suits]
        



    def shuffle(self, **shuffle_and_count):
        """Shuffles the deck using a variety of different shuffles.

        Parameters:
            shuffle_and_count: keyword arguments containing the
            shuffle type and the number of times the shuffled
            should be called.
        """
        assert all(map(lambda shuf_type: True if shuf_type in ['mongean', 'modified_overhand'] else False, shuffle_and_count.keys()))
        assert all(map(lambda num: True if isinstance(num, int) and num > -1 else False, shuffle_and_count.values()))

    

        if 'modified_overhand' in shuffle_and_count:
            self.cards = Shuffle.modified_overhand(self.get_cards(), shuffle_and_count['modified_overhand'])
            #print(shuffle_and_count['modified_overhand'])
        if 'mongean' in shuffle_and_count:
            for i in range(shuffle_and_count['mongean']):
                self.cards = Shuffle.mongean(self.get_cards())

    def deal_hand(self, hand):
        """
        Takes the first card from the deck and adds it to `hand`.
        """
        assert isinstance(hand, PlayerHand)
        first_card = self.cards[0]
        hand.add_card(first_card)
        self.cards.remove(first_card)
        return 

    def get_cards(self):
        return self.cards
