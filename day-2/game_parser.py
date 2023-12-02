import re
from color import Color
from game import Game

class GameParser():
    def __init__(self, input: str):
        self.input = input
        self.games = []

    def parse(self):
        for line in self.input:
            game = Game()
            id, gameplay = line.split(':')
            rounds = gameplay.split(';')

            game.id = self.parse_int(id)
            
            for round in rounds:
                cubes_sets = dict()

                cubes_revealed = round.split(',')
                for cubes in cubes_revealed:
                    color, quantity = self.parse_color_and_quantity(cubes)
                    cubes_sets[color] = quantity

                game.rounds.append(cubes_sets)
            self.games.append(game)

        return self.games
    
    def parse_int(self, id: str) -> int:
        return int(re.sub("[^0-9]", "", id))

    def parse_color_and_quantity(self, cubes: str) -> (str, int):
        color = self.parse_color(cubes)
        quantity = self.parse_int(cubes)
        return color, quantity

    def parse_color(self, cubes: str) -> str:
        for color in Color:
            if color.value in cubes:
                return color.value
