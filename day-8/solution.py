from input_parser import InputParser

START = 'AAA'
END = 'ZZZ'
LEFT = 'L'

def find_path(starting_point, ending_point, network, directions):
    current_node = starting_point
    dir_size = len(directions)

    steps = 0
    while current_node != ending_point:
        left, right = network[current_node]
        current_node = left if directions[steps % dir_size] == LEFT else right
        steps += 1
    
    return steps

def day_8_part_1(input):
    directions, network = InputParser.parse(input)
    print(find_path(START, END, network, directions))

if __name__ == "__main__":
    day_8_part_1(open("inputs/day-8.txt", "r"))
    