from input_parser import InputParser
from mapper import Mapper
from range import Range

SEED = "seed"
LOCATION = "location"

def calculate_seed_to_location_mapping(mappers_by_source, value):
    source = SEED
    while source in mappers_by_source:
        mapper: Mapper = mappers_by_source[source]
        value = mapper.get_mapping(value)
        source = mapper.destination
    return value

def calculate_something_to_seed_mapping(mappers_by_dest, source, value):
    while source != SEED:
        mapper: Mapper = mappers_by_dest[source]
        value = mapper.get_reverse_mapping(value)
        source = mapper.source
    return value

def day_5_part_1(input):
    seed_ranges, mappers_by_source, mappers_by_dest = InputParser.parse(input)

    range_limits = set()

    for seed_range in seed_ranges:
        range_limits.add(seed_range.src_start)
        range_limits.add(seed_range.src_end + 1)

    for mapper in mappers_by_source.values():
        for ranges in mapper.ranges:
            range_limits.add(calculate_something_to_seed_mapping(mappers_by_dest, mapper.source, ranges.src_start))
            range_limits.add(calculate_something_to_seed_mapping(mappers_by_dest, mapper.source, ranges.src_end + 1))
    
    locations = []
    for map_range in range_limits:
        for seed_range in seed_ranges:
            if seed_range.is_within_range(map_range):
                locations.append(calculate_seed_to_location_mapping(mappers_by_source, map_range))

    print(min(locations))



if __name__ == "__main__":
    day_5_part_1(open("inputs/day-5.txt", "r"))
