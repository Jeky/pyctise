#
# Find all connected components in graph
#
from typing import Dict, Set, List
from pprint import pprint
import graph_dict


def link_undirected_edge(graph: Dict[str, Set[str]], node_a: str, node_b: str):
    """ Link two nodes using an undirected edge
    """
    graph_dict.link(graph, node_a, node_b)
    graph_dict.link(graph, node_b, node_a)


def dfs_get_all_connected_nodes(graph: Dict[str, Set[str]], node: str, visited: Set[str]) -> Set[str]:
    """ Get all connected nodes
    """
    stack = [node]
    component = {node}
    while len(stack) > 0:
        cur_node = stack.pop(0)
        if cur_node not in visited:
            for next_node in graph[cur_node]:
                stack.append(next_node)

            visited.add(cur_node)
            component.add(cur_node)

    return component


def find_connected_components(graph: Dict[str, Set[str]]) -> List[Set[str]]:
    """ Find all connected components in graph
    """
    components = []
    visited = set()

    while len(visited) < len(graph):
        start_node = list(graph.keys() - visited)[0]
        components.append(dfs_get_all_connected_nodes(graph, start_node, visited))

    return components


if __name__ == '__main__':
    graph = {}
    link_undirected_edge(graph, 'A', 'B')
    link_undirected_edge(graph, 'B', 'C')
    link_undirected_edge(graph, 'D', 'E')
    pprint(graph)

    print('components:')
    pprint(find_connected_components(graph))
