#
# Output the shortest path between two nodes in the graph. If these two nodes are not connected, return None
#
from typing import Dict, Set
from pprint import pprint
import graph_dict


def find_path(graph: Dict[str, Set[str]], start: str, end: str) -> List[str]:
    """ Find the shortest path between two nodes in the graph. 
        If these two nodes are not connected, return None
    """
    visited = {start}
    queue = [(start, [start])]

    while len(queue) > 0:
        cur_node, path = queue.pop(0)
        if cur_node not in graph:
            return None

        for next_node in graph[cur_node]:
            if next_node == end:
                return path + [next_node]

            if next_node not in visited:
                visited.add(next_node)
                queue.append((next_node, path + [next_node]))

    return None


if __name__ == '__main__':
    graph = {}
    graph_dict.link(graph, 'A', 'B')
    graph_dict.link(graph, 'B', 'C')
    graph_dict.link(graph, 'B', 'D')
    graph_dict.link(graph, 'C', 'D')
    pprint(graph)
    print('From A to C', find_path(graph, 'A', 'C'))
    print('From A to B', find_path(graph, 'A', 'B'))
    print('From B to D', find_path(graph, 'B', 'D'))
    print('From A to D', find_path(graph, 'A', 'D'))
