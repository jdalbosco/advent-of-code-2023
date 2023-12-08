from mapper import Mapper
from range import Range

START_OF_MAP_DEFINITION = 'map'
END_OF_MAP_DEFINITION = '\n'

class InputParser():
    def parse_mappers(self, input):
        mappers_by_source = dict()
        mappers_by_destination = dict()
        mapper = None
        
        line = input.readline()
        while line:
            if START_OF_MAP_DEFINITION in line:
                mapper_name, _ = line.split(' ')
                source, _, destination = mapper_name.split('-')
                mapper = Mapper(source, destination)
            elif line == END_OF_MAP_DEFINITION:
                mappers_by_source[mapper.source] = mapper
                mappers_by_destination[mapper.destination] = mapper
            else:
                dest_start, src_start, range_len = line.split(' ')
                mapper.add_range(Range(int(dest_start), int(src_start), int(range_len)))
            line = input.readline()

        return mappers_by_source, mappers_by_destination
    
    def skip_line(self, input):
        input.readline()