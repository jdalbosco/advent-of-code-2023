from engine.first_engine import FirstEngine
from engine.second_engine import SecondEngine

def day_3_part_1(input):
    engine = FirstEngine.create(input)
    print(engine.run())

def day_3_part_2(input):
    engine = SecondEngine.create(input)
    print(engine.run())

if __name__ == "__main__":
    day_3_part_1(open("inputs/day-3.txt", "r"))
    day_3_part_2(open("inputs/day-3.txt", "r"))
