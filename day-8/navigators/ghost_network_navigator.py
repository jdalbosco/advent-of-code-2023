import math
from navigators.network_navigator import NetworkNavigator

class GhostNetworkNavigator(NetworkNavigator):
    def calculate_number_of_steps(self):
        start_nodes = self.find_nodes_starting_in_A()
        steps_until_end = []

        for start_node in start_nodes:
            steps_until_end.append(self.number_of_steps_to_reach_end(start_node, self.node_ends_in_Z))

        return math.lcm(*steps_until_end)

    def find_nodes_starting_in_A(self):
        start_nodes = []
        for node in self.network:
            if node[-1] == 'A':
                start_nodes.append(node)
        return start_nodes
        
    @staticmethod
    def node_ends_in_Z(node):
        return node[-1] == 'Z'
