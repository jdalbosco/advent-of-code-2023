from hand import Hand
from rankers.hand_node import HandNode
from type import Type

CARD_RANKING = "23456789TJQKA"

class HandRanker():
    def __init__(self):
        self.hand_groups = dict()
        self.total_winnings = 0

    def add_hand(self, hand_to_add: Hand, ranking: str = CARD_RANKING):
        node = self.get_type_head(hand_to_add)

        while node is not None:
            if node.hand.is_higher_than(hand_to_add, ranking):
                if node.left is None:
                    node.left = HandNode(hand_to_add)
                    return
                node = node.left
            else:
                if node.right is None:
                    node.right = HandNode(hand_to_add)
                    return
                node = node.right

    def get_type_head(self, hand: Hand) -> HandNode:
        key = hand.type.name
        if key not in self.hand_groups:
            self.hand_groups[key] = HandNode(hand)
            return None
        
        return self.hand_groups[key]

    def calculate_winnings_by_group(self, head: HandNode):
        if head is None:
            return
        
        self.calculate_winnings_by_group(head.left)
        self.total_winnings += self.rank * head.hand.bid
        self.rank += 1
        self.calculate_winnings_by_group(head.right)

    def calculate_total_winnings(self) -> int:
        self.rank = 1
        for type in Type:
            if type.name in self.hand_groups:
                self.calculate_winnings_by_group(self.hand_groups[type.name])
        return self.total_winnings
