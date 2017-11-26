#
# Convert a graph dict to an adjacency matrix (https://en.wikipedia.org/wiki/Adjacency_matrix)
#
from typing import Dict, Set, List, Tuple
from pprint import pprint
import graph_dict


def create_matrix(width: int, height: int) -> List[List[int]]:
    """ Create a matrix with width and height.
    """
    return [[0 for _ in range(width)] for _ in range(height)]


def print_matrix(matrix: List[List[int]]):
    for line in matrix:
        print(' '.join([str(i) for i in line]))


def to_adj_matrix(graph: Dict[str, Set[str]]) -> Tuple[List[str], List[List[int]]]:
    """ Convert a graph to an adjacency matrix.
        This function will return a matrix header (list of nodes)
        and an adj matrix.
    """
    header = list(graph.keys())
    matrix = create_matrix(len(graph), len(graph))

    for from_node, to_node_list in graph.items():
        from_index = header.index(from_node)
        for to_node in to_node_list:
            to_index = header.index(to_node)
            matrix[from_index][to_index] = 1

    return header, matrix


if __name__ == '__main__':
    graph = {}
    graph_dict.link(graph, 'A', 'B')
    graph_dict.link(graph, 'B', 'C')
    graph_dict.link(graph, 'B', 'D')
    graph_dict.link(graph, 'C', 'D')
    graph_dict.link(graph, 'D', 'A')
    pprint(graph)

    header, matrix = to_adj_matrix(graph)
    pprint(header)
    print_matrix(matrix)
