from hand import Hand
from type import Type

class HandNode():
    def __init__(self, hand: Hand):
        self.hand: Hand = hand
        self.left = None
        self.right = None

class HandRanker():
    def __init__(self):
        self.hand_groups = dict()
        self.total_winnings = 0

    def add_hand(self, hand_to_add: Hand):
        key = hand_to_add.type.name
        
        if key not in self.hand_groups:
            self.hand_groups[key] = HandNode(hand_to_add)
            return
        
        node = self.hand_groups[key]
        while node is not None:
            if node.hand.is_higher_than(hand_to_add):
                if node.left is None:
                    node.left = HandNode(hand_to_add)
                    return
                node = node.left
            else:
                if node.right is None:
                    node.right = HandNode(hand_to_add)
                    return
                node = node.right

    def calculate_winnings_by_group(self, head: HandNode):
        if head is None:
            return
        
        self.calculate_winnings_by_group(head.left)
        self.total_winnings += self.rank * head.hand.bid
        self.rank += 1
        self.calculate_winnings_by_group(head.right)

    def calculate_total_winnings(self):
        self.rank = 1
        for type in Type:
            if type.name in self.hand_groups:
                self.calculate_winnings_by_group(self.hand_groups[type.name])
        return self.total_winnings
