class Shuffle:
    """
    Different kinds of shuffling techniques.
    
    >>> cards = [i for i in range(52)]
    >>> cards[25]
    25
    >>> mod_oh = Shuffle.modified_overhand(cards, 1)
    >>> mod_oh[0]
    25
    >>> mod_oh[25] 
    24
    
    >>> mod_oh1 = Shuffle.modified_overhand(cards, 3)
    >>> mod_oh1[0]
    20
    >>> mod_oh1[25]
    19
    >>> mod_oh1 = Shuffle.modified_overhand(cards, 2)
    >>> mod_oh1[0]
    23
    >>> mod_oh1[25]
    22
    
    >>> cards2 = [i for i in range(5)]
    >>> cards2[0]
    0
    >>> cards2[-1]
    4
    >>> mod = Shuffle.modified_overhand(cards2, 3)
    >>> mod
    [1, 2, 3, 0, 4]
    >>> mong = Shuffle.mongean(mod)
    >>> mong
    [0, 2, 1, 3, 4]
    >>> mod = Shuffle.modified_overhand(cards2, 4)
    >>> mod
    [1, 2, 3, 0, 4]
    >>> mong = Shuffle.mongean(mod)
    >>> mong
    [0, 2, 1, 3, 4]
    >>> mod = Shuffle.modified_overhand(cards2, 2)
    >>> mod
    [0, 1, 2, 3, 4]
    >>> mong = Shuffle.mongean(mod)
    >>> mong
    [3, 1, 0, 2, 4]
    
 
    >>> mongean_shuffle = Shuffle.mongean(mod_oh)
    >>> mongean_shuffle[0]
    51
    >>> mongean_shuffle[26]
    25
    
    >>> mongean_shuff = Shuffle.mongean(list(range(0,11)))
    >>> mongean_shuff
    [9, 7, 5, 3, 1, 0, 2, 4, 6, 8, 10]
    >>> mongean_shuff = Shuffle.mongean(list(range(0,10)))
    >>> mongean_shuff == [9, 7, 5, 3, 1, 0, 2, 4, 6, 8]
    True
    """    


    def modified_overhand(cards, num):
        """
        Takes `num` cards from the middle of the deck and puts them at the
        top. 
        Then decrement `num` by 1 and continue the process till `num` = 0. 
        When num is odd, the "extra" card is taken from the bottom of the
        top half of the deck.
        """
        assert isinstance(num, int) and isinstance(cards, list)
        if num == 0:
            return cards
        start = len(cards)//2 - num//2
        end = len(cards)//2 + num//2
        if len(cards) % 2 != 0 and num % 2 != 0:
            end += 1
        elif len(cards) % 2 == 0 and num % 2 != 0:
            start -= 1
        alt_card = cards[start:end] + cards[:start] + cards[end:]
        return Shuffle.modified_overhand(alt_card, num - 1)


    def mongean(cards):
        """
        Implements the mongean shuffle. 

        """
        
        if cards == []:
            return []
        if len(cards) % 2 != 0: 
            return Shuffle.mongean(cards[:-1]) + [cards[-1]] 
        else: 
            return [cards[-1]] + Shuffle.mongean(cards[:-1])
