class Range():
    def __init__(self, dest_start: int, src_start: int, range_len: int):
        self.dest_start = dest_start
        self.src_start = src_start
        self.dest_end = dest_start + range_len - 1
        self.src_end = src_start + range_len - 1

    def get_mapping(self, value) -> int:
        offset = value - self.src_start
        return self.dest_start + offset

    def is_within_range(self, value) -> bool:
        return value >= self.src_start and value <= self.src_end
