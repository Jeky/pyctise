#
# A famous ranking algorithm named after Larry Page. This algorithm is the foundation of Google (At the beginning time).
# There are many ways to compute the ranking values. In this program we are using random walking, which is also a Monte Carlo method.
#
import random
import graph_dict
from typing import Dict, List

def random_jump(graph: Dict[str, List[str]]) -> str:
    """ Random jumping to a node"""
    return random.choice(list(graph.keys()))


def random_walk(graph: Dict[str, List[str]], iteration_count: int = 10000, random_jump_ratio: float = 0.1) -> Dict[str, int]:
    """ Random walking on the graph with a random start. 
        Returns the mapping from node to visited times of this node.
    """
    visited = {}
    for node in graph.keys():
        visited[node] = 0

    current = random_jump(graph)
    visited[current] += 1

    for i in range(iteration_count):
        next_nodes = list(graph[current])
        jump_chance = random.random()

        if len(next_nodes) != 0 and jump_chance >= random_jump_ratio:
            current = random.choice(next_nodes)
        else:
            current = random_jump(graph)

        visited[current] += 1

    return visited


def get_sorting_key(item):
    return -item[1]


def print_ranking(visited_dict: Dict[str, int]):
    total_visit_count = 0
    visited_list = []

    for node, count in visited_dict.items():
        total_visit_count += count
        visited_list.append([node, count])

    # normalizing
    for item in visited_list:
        item[1] /= total_visit_count

    # sort by normalized count in desc order
    visited_list.sort(key=get_sorting_key)
    for item in visited_list:
        print('{}: {}'.format(item[0], item[1]))


if __name__ == '__main__':
    graph = {}
    graph_dict.link(graph, 'A', 'B')
    graph_dict.link(graph, 'A', 'C')
    graph_dict.link(graph, 'B', 'D')
    graph_dict.link(graph, 'C', 'D')
    graph_dict.link(graph, 'D', 'E')
    graph_dict.link(graph, 'C', 'A')

    visited_dict = random_walk(graph)
    print_ranking(visited_dict)
