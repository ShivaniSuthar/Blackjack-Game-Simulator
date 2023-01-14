class Card:
    """
    Card class.

    # Doctests for str and repr
    >>> card_1 = Card("A", "spades")
    >>> print(card_1)
    ____
    |A  |
    | ♠ |
    |__A|
    >>> card_1
    (A, spades)
    >>> card_2 = Card("K", "spades")
    >>> print(card_2)
    ____
    |K  |
    | ♠ |
    |__K|
    >>> card_2
    (K, spades)
    >>> card_3 = Card("A", "diamonds")
    >>> print(card_3)
    ____
    |A  |
    | ♦ |
    |__A|
    >>> card_3
    (A, diamonds)

    # Doctests for comparisons
    >>> card_1 < card_2
    False
    >>> card_1 > card_2
    True
    >>> card_3 > card_1
    False

    # Doctests for set_visible()
    >>> card_3.set_visible(False)
    >>> print(card_3)
    ____
    |?  |
    | ? |
    |__?|
    >>> card_3
    (?, ?)
    >>> card_3.set_visible(True)
    >>> print(card_3)
    ____
    |A  |
    | ♦ |
    |__A|
    >>> card_3
    (A, diamonds)
    
    >>> card_4 = Card(4, "spades")
    >>> print(card_4)
    ____
    |4  |
    | ♠ |
    |__4|
    >>> card_4
    (4, spades)
    >>> card_5 = Card(5, "spades", visible=False)
    >>> print(card_5)
    ____
    |?  |
    | ? |
    |__?|
    >>> card_5
    (?, ?)
    
    >>> Card(7, "")
    Traceback (most recent call last):
    ...
    AssertionError
    """

    # Class Attribute(s)

    def __init__(self, rank, suit, visible=True):
        """
        Creates a card instance and asserts that the rank and suit are valid.
        """
        assert rank in list(range(2, 11)) + ['A', 'J', 'Q', 'K']
        assert suit in ['spades', 'diamonds', 'hearts', 'clubs']
        assert isinstance(visible, bool)
        self.rank = rank
        self.suit = suit
        self.visible = visible

    def __lt__(self, other_card):
        if self.get_rank() == '?':
            return 'cannot compare'
        temp_rank_self = self.get_rank()
        temp_rank_other_card = other_card.get_rank()
        if self.get_rank() == other_card.get_rank():
            suit_self = self.get_suit()
            suit_other = other_card.get_suit()
            if suit_self == 'diamonds':
                suit_self = 2
            elif suit_self == 'spades':
                suit_self = 4
            elif suit_self == 'clubs':
                suit_self = 1
            elif suit_self == 'hearts':
                suit_self = 3
            if suit_other == 'diamonds':
                suit_other = 2
            elif suit_other == 'spades':
                suit_other = 4
            elif suit_other == 'clubs':
                suit_other = 1
            elif suit_other == 'hearts':
                suit_other = 3
            return suit_self < suit_other
        if temp_rank_self == 'A':
            temp_rank_self = 14
        elif temp_rank_self == 'K':
            temp_rank_self = 13
        elif temp_rank_self == 'Q':
            temp_rank_self = 12
        elif temp_rank_self == 'J':
            temp_rank_self = 11
        if temp_rank_other_card == 'A':
            temp_rank_other_card = 14
        elif temp_rank_other_card == 'K':
            temp_rank_other_card = 13
        elif temp_rank_other_card == 'Q':
            temp_rank_other_card = 12
        elif temp_rank_other_card == 'J':
            temp_rank_other_card = 11
        return temp_rank_self < temp_rank_other_card


    def __str__(self):
        """
        Returns ASCII art of a card with the rank and suit. If the card is
        hidden, question marks are put in place of the actual rank and suit.

        Examples:
        ____
        |A  |
        | ♠ |
        |__A|
        ____
        |?  |
        | ? |
        |__?|             
        """
        if self.get_suit() == 'diamonds':
            suit = '♦'
        elif self.get_suit() == 'spades':
            suit = '♠'
        elif self.get_suit() == 'hearts':
            suit = '♥'
        elif self.get_suit() == 'clubs':
            suit = '♣'
        if self.visible:
            return '\n'.join(['____', '|{}  |'.format(self.get_rank()), \
            '| {} |'.format(suit), '|__{}|'.format(self.get_rank())]).strip('\n')
        elif not self.visible:
            return '\n'.join(['____', '|?  |', '| ? |', '|__?|']).strip('\n')

    def __repr__(self):
        """
        Returns (<rank>, <suit>). If the card is hidden, question marks are
        put in place of the actual rank and suit.           
        """        
        if self.visible:
            return '(' + str(self.get_rank()) + ', ' + self.get_suit() + ')'
        elif not self.visible:
            return '(?, ?)'

    def get_rank(self):
        return self.rank

    def get_suit(self):
        return self.suit

    def set_visible(self, visible):
        assert isinstance(visible, bool)
        self.visible = visible
