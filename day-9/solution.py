FORWARDS = 1
BACKWARDS = -1

def parse(line):
    return [int(value) for value in line.split(' ')]

def calculate_differences(history):
    differences = []
    for i in range(1, len(history)):
        differences.append(history[i] - history[i-1])
    return differences

def extrapolate(history):
    if all(value == 0 for value in history):
        return 0
    return history[-1] + extrapolate(calculate_differences(history))

def sum_predictions(input, direction):
    sum_of_predictions = 0

    for line in input:
        history = parse(line)
        sum_of_predictions += extrapolate(history[::direction])

    return sum_of_predictions

def day_9_part_1(input):
    print(sum_predictions(input, FORWARDS))

def day_9_part_2(input):
    print(sum_predictions(input, BACKWARDS))

if __name__ == "__main__":
    day_9_part_1(open("inputs/day-9.txt", "r"))
    day_9_part_2(open("inputs/day-9.txt", "r"))
