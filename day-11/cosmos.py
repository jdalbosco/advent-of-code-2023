import re

EMPTY_SPACE = '.'
GALAXY = '#'

VERTICAL = 0
HORIZONTAL = 1

class Cosmos():
    def __init__(self):
        self.image = []
        self.galaxies = set()

    @staticmethod
    def process_image(input):
        cosmos = Cosmos()
        for line in input:
            cosmos.image.append(re.sub('[^.#]', '', line))
        return cosmos
    
    def map_galaxies(self):
        self.galaxies = set()
        for row, line in enumerate(self.image):
            columns = [column.start() for column in re.finditer('#', line)]
            for column in columns:
                self.galaxies.add((row, column))

    def update_galaxy_positions(self, positions, expansion_rate, direction):
        for position in positions[::-1]:
            for galaxy in list(self.galaxies):
                row, column = galaxy
                if direction == VERTICAL and row > position:
                    row += expansion_rate - 1
                if direction == HORIZONTAL and column > position:
                    column += expansion_rate - 1
                self.galaxies.remove(galaxy)
                self.galaxies.add((row, column))

    def expand_vertically(self, expansion_rate):
        rows_to_duplicate = []
        for row_number, row in enumerate(self.image):
            if all(element == EMPTY_SPACE for element in row):
                rows_to_duplicate.append(row_number)
        
        self.update_galaxy_positions(rows_to_duplicate, expansion_rate, VERTICAL)

    def expand_horizontally(self, expansion_rate):
        def is_all_empty_spaces(column):
            rows = len(self.image)
            for row in range(rows):
                if self.image[row][column] != EMPTY_SPACE:
                    return False
            return True

        columns = len(self.image[0])
        columns_to_duplicate = []
        for column_number in range(columns):
            if is_all_empty_spaces(column_number):
                columns_to_duplicate.append(column_number)

        self.update_galaxy_positions(columns_to_duplicate, expansion_rate, HORIZONTAL)

    def expand(self, expansion_rate):
        self.map_galaxies()
        self.expand_vertically(expansion_rate)
        self.expand_horizontally(expansion_rate)

    def calculate_distance_between(self, first_galaxy, second_galaxy):
        first_row, first_column = first_galaxy
        second_row, second_column = second_galaxy
        return abs(first_row - second_row) + abs(first_column - second_column)
    
    def calculate_all_paths(self):
        distance = 0
        while len(self.galaxies) > 0:
            first_galaxy = self.galaxies.pop()
            for second_galaxy in self.galaxies:
                distance += self.calculate_distance_between(first_galaxy, second_galaxy)
        
        return distance
