from type import Type

CARD_RANKING = "23456789TJQKA"

class Hand():
    def __init__(self, hand: str, bid: int):
        self.cards = hand
        self.bid = bid
        self.type = None

    @staticmethod
    def create(hand: str, bid: int):
        hand = Hand(hand, bid)
        hand.type = hand.find_hand_type()
        return hand

    def find_hand_type(self) -> Type:
        hand = dict()
        for card in self.cards:
            if card not in hand:
                hand[card] = 0
            hand[card] += 1
        
        labels, amounts = len(hand), set(hand.values())

        for type in Type:
            type_labels, type_amounts = type.value
            if type_labels == labels and type_amounts == amounts:
                return type

    def is_higher_than(self, hand):
        for index in range(5):
            this_card = self.cards[index]
            other_card = hand.cards[index]
            if this_card != other_card:
                return CARD_RANKING.find(this_card) > CARD_RANKING.find(other_card)
        return False
