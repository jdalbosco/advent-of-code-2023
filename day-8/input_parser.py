import re

class InputParser():
    @staticmethod
    def parse(input) -> (str, dict):
        def clean(string):
            return re.sub('[^A-Z]', '', string)
    
        directions = clean(input.readline())
        network = dict()

        input.readline()

        for line in input:
            node, connections = line.split('=')
            left, right = connections.split(',')
            network[clean(node)] = (clean(left), clean(right))

        return directions, network
