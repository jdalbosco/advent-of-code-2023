from hand import Hand
from rankers.hand_node import HandNode
from rankers.hand_ranker import HandRanker
from type import Type

JOKER = "J"
ALL_JOKERS = "JJJJJ"
CARD_RANKING = "J23456789TQKA"

class HandRankerWithJoker(HandRanker):
    def add_hand(self, hand: Hand):
        if JOKER in hand.cards:
            self.deal_with_jokers(hand)

        super().add_hand(hand, CARD_RANKING)

    def deal_with_jokers(self, hand):
        if hand.cards == ALL_JOKERS:
            hand.type = Type.FIVE_OF_A_KIND
            return
            
        number_of_jokers = hand.cards.count(JOKER)
        number_of_labels, amounts = hand.type.value
        number_of_labels -= 1
        hand_amounts = amounts.copy()
        hand_amounts.remove(number_of_jokers)
        hand_amounts[-1] += number_of_jokers
            
        for type in Type:
            type_labels, type_amounts = type.value
            if type_labels == number_of_labels and type_amounts == hand_amounts:
                hand.type = type