from hand import Hand

class HandNode():
    def __init__(self, hand: Hand):
        self.hand: Hand = hand
        self.left = None
        self.right = None