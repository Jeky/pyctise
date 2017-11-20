#
# Invert a graph (from_node to to_node_list) to graph (to_node to from_node_list).
#
# GRAPH: {
#   'A' : ['B', 'C', 'D'],
#   'B' : ['C'],
#   'C' : ['A', 'D'],
#   'D' : ['A', 'B', 'E']
# }
# will be inverted to
# {
#   'A': ['C', 'D'],
#   'B': ['A', 'D'],
#   'C': ['A', 'B'],
#   'D': ['A', 'C'],
#   'E': ['D']
# }
from typing import Dict, List


def invert(graph: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """ Invert a graph
    """
    inverted = {}
    for from_node, to_node_list in graph.items():
        for to_node in to_node_list:
            if to_node not in inverted:
                inverted[to_node] = []

            if from_node not in inverted[to_node]:
                inverted[to_node].append(from_node)

    return inverted


if __name__ == '__main__':
    graph = {
        'A': ['B', 'C', 'D'],
        'B': ['C'],
        'C': ['A', 'D'],
        'D': ['A', 'B', 'E']
    }

    print(invert(graph))
