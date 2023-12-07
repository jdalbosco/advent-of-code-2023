from enum import Enum

class Type(Enum):
    HIGH_CARD = (5, {1, 1, 1, 1, 1})
    ONE_PAIR = (4, {2, 1, 1, 1})
    TWO_PAIR = (3, {2, 2, 1})
    THREE_OF_A_KIND = (3, {3, 1, 1})
    FULL_HOUSE = (2, {3, 2})
    FOUR_OF_A_KIND = (2, {4, 1})
    FIVE_OF_A_KIND = (1, {5})
