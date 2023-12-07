import re

class Race():
    def __init__(self, duration, distance):
        self.duration = duration
        self.record_distance = distance
    
    def distance_traveled(self, time_holding_button):
        speed = time_holding_button
        time_moving = self.duration - time_holding_button
        return time_moving * speed
    
    def race_duration_is_even(self):
        return self.duration % 2

    def calculate_ways_to_beat(self, min_time_holding_to_win):
        additional_way_to_beat = 0 if self.race_duration_is_even() else 1
        possible_times_holding_button = (self.duration + 1)
        ways_to_beat = (possible_times_holding_button // 2 - min_time_holding_to_win) * 2
        return ways_to_beat + additional_way_to_beat

    def ways_to_beat(self):
        for time_holding_button in range((self.duration + 1) // 2):
            if self.distance_traveled(time_holding_button) > self.record_distance:
                return self.calculate_ways_to_beat(time_holding_button)
        return 0


def part_1(input_durations, input_distances):
    durations = [int(duration) for duration in input_durations.strip().split(' ') if duration != '']
    distances = [int(distance) for distance in input_distances.strip().split(' ') if distance != '']

    margin_of_error = 1
    for race_number, distance in enumerate(distances):
        race = Race(durations[race_number], distance)
        margin_of_error *= race.ways_to_beat()

    return margin_of_error
 
def part_2(input_duration, input_distance):
    duration = int(re.sub('[^0-9]', '', input_duration))
    distance = int(re.sub('[^0-9]', '', input_distance))
    race = Race(duration, distance)
    return race.ways_to_beat()

if __name__ == "__main__":
    input = open("inputs/day-6.txt", "r")
    _, input_duration = input.readline().split(':')
    _, input_distance = input.readline().split(':')

    print(part_1(input_duration, input_distance))
    print(part_2(input_duration, input_distance))