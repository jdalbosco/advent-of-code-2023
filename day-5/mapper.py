from range import Range

class Mapper():
    def __init__(self, source: str, destination: str):
        self.source = source
        self.destination = destination
        self.ranges = []

    def add_range(self, range: Range):
        self.ranges.append(range)

    def get_mapping(self, value) -> int:
        for range in self.ranges:
            if range.is_within_source_range(value):
                return range.get_mapping(value)
        return value

    def get_reverse_mapping(self, value) -> int:
        for range in self.ranges:
            if range.is_within_destination_range(value):
                return range.get_reverse_mapping(value)
        return value