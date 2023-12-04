import re
from scratchcard import Scratchcard

class ScratchcardParser():
    def parse(self, game_line: str) -> Scratchcard:
        id_str, card_str = game_line.split(':')
        winning_numbers_str, scratched_numbers_str = card_str.split(' | ')

        id = self.parse_int(id_str)
        winning_numbers = [self.parse_int(number) for number in self.clean(winning_numbers_str).split(' ')]
        scratched_numbers = [self.parse_int(number) for number in self.clean(scratched_numbers_str).split(' ')]

        return Scratchcard(id, set(winning_numbers), set(scratched_numbers))
    
    def parse_int(self, str: str) -> int:
        return int(re.sub("[^0-9]", "", str))
    
    def clean(self, str: str) -> str:
        return re.sub("  ", " ", str).strip()
