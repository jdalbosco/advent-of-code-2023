LEFT = 'L'

class NetworkNavigator():
    def __init__(self, network, directions):
        self.network = network
        self.directions = directions

    def calculate_number_of_steps(self):
        return self.number_of_steps_to_reach_end('AAA', self.node_is_ZZZ)

    def number_of_steps_to_reach_end(self, start_point, end_condition):
        current_node = start_point
        dir_size = len(self.directions)

        steps = 0
        while not end_condition(current_node):
            left, right = self.network[current_node]
            current_node = left if self.directions[steps % dir_size] == LEFT else right
            steps += 1
        
        return steps
    
    @staticmethod
    def node_is_ZZZ(node):
        return node == 'ZZZ'