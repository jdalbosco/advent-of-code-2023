from hand import Hand
from rankers.hand_ranker import HandRanker
from rankers.hand_ranker_with_jokers import HandRankerWithJoker

def rank_and_calculate_winnings(input, ranker):
    for line in input:
        hand, bid = line.split(' ')
        ranker.add_hand(Hand.create(hand, int(bid)))
    return ranker.calculate_total_winnings()

def day_7_part_2(input):
    print(rank_and_calculate_winnings(input, HandRankerWithJoker()))

def day_7_part_1(input):
    print(rank_and_calculate_winnings(input, HandRanker()))

if __name__ == "__main__":
    day_7_part_1(open("inputs/day-7.txt", "r"))
    day_7_part_2(open("inputs/day-7.txt", "r"))