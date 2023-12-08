from type import Type

JOKER = "J"
ALL_JOKERS = "JJJJJ"
CARD_RANKING = "J23456789TJQKA"

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
            
        labels, amounts = len(hand), sorted(hand.values())

        if JOKER in hand:
            if self.cards == ALL_JOKERS:
                return Type.FIVE_OF_A_KIND
            labels, amounts = self.deal_with_jokers(hand, labels, amounts)

        for type in Type:
            type_labels, type_amounts = type.value
            if type_labels == labels and type_amounts == amounts:
                return type

    def deal_with_jokers(self, hand, labels, amounts):
        jokers = hand.pop(JOKER)
        labels -= 1
        amounts.remove(jokers)
        amounts[-1] += jokers
        return labels, amounts

    def is_higher_than(self, hand):
        for index in range(5):
            this_card = self.cards[index]
            other_card = hand.cards[index]
            if this_card != other_card:
                return CARD_RANKING.find(this_card) > CARD_RANKING.find(other_card)
        return False
