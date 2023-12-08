from parsers.input_parser import InputParser
from range import Range

class InputParserForPart2(InputParser):
    @staticmethod
    def create(input):
        input_parser = InputParserForPart2()
        seed_ranges = input_parser.parse_seed_ranges(input)
        input_parser.skip_line(input)
        mappers_by_source, mappers_by_destination = input_parser.parse_mappers(input)
        return seed_ranges, mappers_by_source, mappers_by_destination
    
    def parse_seed_ranges(self, input):
        _, seeds_input = input.readline().split(': ')
        seeds_input = [int(seed) for seed in seeds_input.split(' ')]

        seed_ranges = []
        for i in range(len(seeds_input)//2):
            range_start = seeds_input[i*2]
            range_length = seeds_input[i*2+1]
            seed_ranges.append(Range(range_start, range_start, range_length))

        return seed_ranges