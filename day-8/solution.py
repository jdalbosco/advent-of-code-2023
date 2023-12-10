from input_parser import InputParser
from navigators.network_navigator import NetworkNavigator
from navigators.ghost_network_navigator import GhostNetworkNavigator


def day_8_part_1(network, directions):
    navigator = NetworkNavigator(network, directions)
    print(navigator.calculate_number_of_steps())

def day_8_part_2(network, directions):
    navigator = GhostNetworkNavigator(network, directions)
    print(navigator.calculate_number_of_steps())

if __name__ == "__main__":
    directions, network = InputParser.parse(open("inputs/day-8.txt", "r"))
    day_8_part_1(network, directions)
    day_8_part_2(network, directions)
