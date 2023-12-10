import re

class InputParser():
    @staticmethod
    def parse(input) -> (str, dict):
        def clean(string):
            return re.sub('[^A-Z=,]', '', string)
    
        directions = clean(input.readline())
        network = dict()

        input.readline()

        for line in input:
            node, connections = clean(line).split('=')
            left, right = connections.split(',')
            network[node] = (left, right)

        return directions, network
