REVERSED = -1
NOT_REVERSED = 1

SPELLED_NUMBER_TO_DIGIT = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def get_first_specific_number(line, spelled, digit):
    NOT_FOUND = -1
    MAX_IDX = len(line)
    
    first_digit, first_spelled = line.find(digit), line.find(spelled)
    first_digit = MAX_IDX if first_digit is NOT_FOUND else first_digit
    first_spelled = MAX_IDX if first_spelled is NOT_FOUND else first_spelled

    return min(first_digit, first_spelled)

def get_first_number(line, reversed = NOT_REVERSED):
    first_number, first_number_idx = 0, len(line)

    for spelled, digit in SPELLED_NUMBER_TO_DIGIT.items():
        first_specific_number_idx = get_first_specific_number(line[::reversed], spelled[::reversed], digit)

        if first_number_idx > first_specific_number_idx:
            first_number_idx = first_specific_number_idx
            first_number = digit

    return first_number

def day_1(input):
    sum = 0
    for line in input:
        first_number = get_first_number(line)
        last_number = get_first_number(line, REVERSED)
        sum += int(first_number + last_number)

    print(sum)

if __name__ == "__main__":
    input = open("inputs/day-1.txt", "r")
    day_1(input)
