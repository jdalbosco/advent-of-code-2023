from parsers.input_parser_for_part_1 import InputParserForPart1
from parsers.input_parser_for_part_2 import InputParserForPart2
from mapper import Mapper

SEED = "seed"
LOCATION = "location"

def calculate_seed_to_location_mapping(mappers_by_source, value):
    source = SEED
    while source in mappers_by_source:
        mapper: Mapper = mappers_by_source[source]
        value = mapper.get_mapping(value)
        source = mapper.destination
    return value

def backtrack_to_seed(mappers_by_dest, source, value):
    while source != SEED:
        mapper: Mapper = mappers_by_dest[source]
        value = mapper.get_reverse_mapping(value)
        source = mapper.source
    return value



def day_5_part_1(input):
    seeds, mappers_by_source = InputParserForPart1.create(input)
    
    locations = []
    for seed_value in seeds:
        locations.append(calculate_seed_to_location_mapping(mappers_by_source, seed_value))

    print(min(locations))

def day_5_part_2(input):
    seed_ranges, mappers_by_source, mappers_by_dest = InputParserForPart2.create(input)

    range_limits = set()

    for mapper in mappers_by_source.values():
        for ranges in mapper.ranges:
            new_range_start = backtrack_to_seed(mappers_by_dest, mapper.source, ranges.src_start)
            new_range_end = backtrack_to_seed(mappers_by_dest, mapper.source, ranges.src_end + 1)
            range_limits.add(new_range_start)
            range_limits.add(new_range_end)
    
    locations = []
    for range_start in range_limits:
        for seed_range in seed_ranges:
            if seed_range.is_within_source_range(range_start):
                locations.append(calculate_seed_to_location_mapping(mappers_by_source, range_start))

    print(min(locations))



if __name__ == "__main__":
    day_5_part_1(open("inputs/day-5.txt", "r"))
    day_5_part_2(open("inputs/day-5.txt", "r"))
