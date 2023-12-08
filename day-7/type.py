from enum import Enum

class Type(Enum):
    HIGH_CARD = (5, [1, 1, 1, 1, 1])
    ONE_PAIR = (4, [1, 1, 1, 2])
    TWO_PAIR = (3, [1, 2, 2])
    THREE_OF_A_KIND = (3, [1, 1, 3])
    FULL_HOUSE = (2, [2, 3])
    FOUR_OF_A_KIND = (2, [1, 4])
    FIVE_OF_A_KIND = (1, [5])
