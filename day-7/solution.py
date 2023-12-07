from hand import Hand
from hand_ranker import HandRanker

def day_7_part_1(input):
    ranker = HandRanker()

    for line in input:
        hand, bid = line.split(' ')
        ranker.add_hand(Hand.create(hand, int(bid)))

    print(ranker.calculate_total_winnings())

if __name__ == "__main__":
    day_7_part_1(open("inputs/day-7.txt", "r"))
