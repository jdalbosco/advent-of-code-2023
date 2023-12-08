from parsers.input_parser import InputParser

class InputParserForPart1(InputParser):
    @staticmethod
    def create(input):
        input_parser = InputParserForPart1()
        seeds = input_parser.parse_seeds(input)
        input_parser.skip_line(input)
        mappers_by_source, _ = input_parser.parse_mappers(input)
        return seeds, mappers_by_source
    
    def parse_seeds(self, input):
        _, seeds = input.readline().split(': ')
        return [int(seed) for seed in seeds.split(' ')]