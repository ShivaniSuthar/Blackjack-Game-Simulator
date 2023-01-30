from card import Card

class PlayerHand():
    """
    >>> card_1 = Card("A", "spades")
    >>> card_2 = Card(2, "diamonds")
    >>> card_3 = Card(3, "clubs")
    >>> card_4 = Card(4, "hearts")
    >>> card_5 = Card(5, "spades")
    >>> card_6 = Card("K", "diamonds")
    >>> card_7 = Card("J", "clubs")
    >>> card_8 = Card("Q", "hearts")
    
    >>> p_hand = PlayerHand()
    >>> p_hand.add_card(card_1, card_2)
    >>> p_hand
    (2, diamonds) (A, spades)
    >>> p_hand.add_card(card_3)
    >>> print(p_hand)
    ____
    |2  |
    | ♦ |
    |__2|
    ____
    |3  |
    | ♣ |
    |__3|
    ____
    |A  |
    | ♠ |
    |__A|
    
    >>> p_hand
    (2, diamonds) (3, clubs) (A, spades)

    >>> d_hand = DealerHand()
    >>> d_hand.add_card(card_4)
    >>> d_hand.add_card(card_5, card_6)
    >>> print(d_hand)
    ____
    |4  |
    | ♥ |
    |__4|
    ____
    |?  |
    | ? |
    |__?|
    ____
    |?  |
    | ? |
    |__?|
    >>> d_hand
    (4, hearts) (?, ?) (?, ?)
    >>> d_hand.reveal_hand()
    >>> print(d_hand)
    ____
    |4  |
    | ♥ |
    |__4|
    ____
    |5  |
    | ♠ |
    |__5|
    ____
    |K  |
    | ♦ |
    |__K|
    >>> d_hand
    (4, hearts) (5, spades) (K, diamonds)
    
    >>> p_hand_2 = PlayerHand()
    >>> p_hand_2.sort_hand()
    >>> print(p_hand_2)
    []
    >>> p_hand_2
    []
    >>> p_hand_2.add_card()
    >>> print(p_hand_2)
    []
    >>> p_hand_2
    []
    >>> p_hand_2.add_card(Card(7, 'diamonds'))
    >>> p_hand_2.add_card(Card(5, 'spades'))
    >>> p_hand_2.add_card(Card('K', 'hearts'))
    >>> p_hand_2.add_card(Card(7, 'clubs'))
    >>> p_hand_2.sort_hand()
    >>> print(p_hand_2)
    ____
    |5  |
    | ♠ |
    |__5|
    ____
    |7  |
    | ♣ |
    |__7|
    ____
    |7  |
    | ♦ |
    |__7|
    ____
    |K  |
    | ♥ |
    |__K|
    >>> p_hand_2
    (5, spades) (7, clubs) (7, diamonds) (K, hearts)
    """

    def __init__(self):
        self.cards = []


    def add_card(self, *cards):
        """
        Adds cards to the hand, then sorts
        them in ascending order.
        """
        for card in cards:
            assert isinstance(card, Card)
            self.cards.append(card)
        self.sort_hand()

    def get_cards(self):
        return self.cards           

    def __str__(self):
        """
        Returns the string representation of all cards
        in the hand, with each card on a new line.
        """
        if len(self.get_cards()) == 0:
            return '[]'
        return "\n".join(list((map(str, self.get_cards()))))
    
    def __repr__(self):
        """
        Returns the representation of all cards, with 
        each card separated by a space.
        """
        if len(self.get_cards()) == 0:
            return '[]'
        return " ".join(list((map(repr, self.cards))))

    def sort_hand(self):
        """
        Sorts the cards in ascending order.
        """

        return self.cards.sort()

class DealerHand(PlayerHand):
    
    def __init__(self):
    
        super().__init__()
        self.hand_revealed = False

    def add_card(self, *cards):
        """
        Adds the cards to hand such that only the first card
        in the hand is visible (when the dealer's hand is not visible).
        If the dealer's hand is visible, then add cards to hand as 
        usual and sort them in ascending order.
        """
        if len(cards) == 0:
            return
        assert all(list(map(lambda x: isinstance(x, Card), cards)))

        if self.hand_revealed:
            super().add_card(*cards)
        else:
            for card in cards:
                if len(self.cards) != 0:
                    card.set_visible(False)
                    self.cards.append(card)
                else:
                    card.set_visible(True)
                    self.cards.append(card)


    def reveal_hand(self):
        """
        Makes all the cards in the hand visible
        and sorts them in ascending order.
        """
        for card in self.cards:
            card.set_visible(True)
        self.hand_revealed = True
        self.sort_hand()
