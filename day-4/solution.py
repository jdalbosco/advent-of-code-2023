from collections import deque
from scratchcard_parser import ScratchcardParser

def day_4_part_2(input):
    parser = ScratchcardParser()
    copies_generated_by_card = dict()
    numbers_to_process = deque()

    for line in input:
        card = parser.parse(line)
        copies_generated_by_card[card.number] = card.calculate_copied_cards()
        numbers_to_process.append(card.number)

    pile_size = 0

    while len(numbers_to_process) > 0:
        number = numbers_to_process.pop()
        numbers_to_process.extend(copies_generated_by_card[number])
        pile_size += 1

    print(pile_size)

def day_4_part_1(input):
    parser = ScratchcardParser()
    points = 0

    for line in input:
        card = parser.parse(line)
        points += card.calculate_points()

    print(points)

if __name__ == "__main__":
    day_4_part_1(open("inputs/day-4.txt", "r"))
    day_4_part_2(open("inputs/day-4.txt", "r"))
