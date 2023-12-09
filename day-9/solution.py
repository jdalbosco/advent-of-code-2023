def calculate_differences(history):
    differences = []
    for i in range(1, len(history)):
        differences.append(history[i] - history[i-1])
    return differences

def calculate_prediction(history):
    if all(value == 0 for value in history):
        return 0
    return history[-1] + calculate_prediction(calculate_differences(history))

def parse(line):
    return [int(value) for value in line.split(' ')]

if __name__ == "__main__":
    input = open("inputs/day-9.txt", "r")
    
    sum_of_predictions = 0

    for line in input:
        history = parse(line)
        sum_of_predictions += calculate_prediction(history)

    print(sum_of_predictions)
