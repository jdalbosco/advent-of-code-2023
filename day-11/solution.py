from cosmos import Cosmos

def day_11_part_1(input):
    cosmos = Cosmos.process_image(input)
    cosmos.expand(2)
    print(cosmos.calculate_all_paths())

def day_11_part_2(input):
    cosmos = Cosmos.process_image(input)
    cosmos.expand(1000000)
    print(cosmos.calculate_all_paths())

if __name__ == "__main__":
    day_11_part_1(open("inputs/day-11.txt", "r"))
    day_11_part_2(open("inputs/day-11.txt", "r"))
