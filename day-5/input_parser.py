from mapper import Mapper
from range import Range

class InputParser():
    def __init__(self):
        self.seeds = [int]
        self.mappers_by_source = dict()

    @staticmethod
    def parse(input):
        input_parser = InputParser()
        _, seeds = input.readline().split(': ')
        input_parser.seeds = [int(seed) for seed in seeds.split(' ')]

        mapper = None
        line = input.readline()
        line = input.readline()

        while line:
            if line == '\n':
                input_parser.mappers_by_source[mapper.source] = mapper
            elif "map" in line:
                mapper_name, _ = line.split(' ')
                source, _, destination = mapper_name.split('-')
                mapper = Mapper(source, destination)
            else:
                dest_start, src_start, range_len = line.split(' ')
                mapper.add_range(Range(int(dest_start), int(src_start), int(range_len)))
            line = input.readline()
        input_parser.mappers_by_source[mapper.source] = mapper

        return input_parser.seeds, input_parser.mappers_by_source
