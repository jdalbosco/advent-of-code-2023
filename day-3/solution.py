from engine.engine import Engine

def day_3_part_1(input):
    engine = Engine()
    engine.process_schematic(input)

    sum = 0
    for number in engine.numbers:
        if engine.is_part_number(number):
            sum += number.value

    print(sum)

def day_3_part_2(input):
    engine = Engine()
    engine.process_schematic(input)

    sum = 0
    for number in engine.numbers:
        engine.connect_to_gear(number)

    for gear in engine.gears.values():
        if len(gear) == 2:
            sum += gear[0] * gear[1]

    print(sum)

if __name__ == "__main__":
    day_3_part_1(open("inputs/day-3.txt", "r"))
    day_3_part_2(open("inputs/day-3.txt", "r"))
