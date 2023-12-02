from game_parser import GameParser

def day_2_part_1(games, bag):
    sum_of_ids = 0

    for game in games:
        if game.is_possible(bag):
            sum_of_ids += game.id
    
    print(sum_of_ids)

def day_2_part_2(games):
    power_sum = 0

    for game in games:
        power_sum += game.calculate_power()

    print(power_sum)


if __name__ == "__main__":
    input = open("inputs/day-2.txt", "r")
    parser = GameParser(input)

    games = parser.parse()
    bag = {"red": 12, "green": 13, "blue": 14}
    
    day_2_part_1(games, bag)
    day_2_part_2(games)