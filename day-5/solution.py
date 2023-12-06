from input_parser import InputParser
from mapper import Mapper

SEED = "seed"
LOCATION = "location"

def day_5_part_1(input):
    seeds, mappers_by_source = InputParser.parse(input)
    locations = []

    for seed in seeds:
        value = seed
        source = SEED
        while source in mappers_by_source:
            mapper: Mapper = mappers_by_source[source]
            value = mapper.get_mapping(value)
            source = mapper.destination
        locations.append(value)

    print(min(locations))

if __name__ == "__main__":
    day_5_part_1(open("inputs/day-5.txt", "r"))
