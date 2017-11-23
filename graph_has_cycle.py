#
# Test if there is a cycle in the graph
#
from typing import Dict, List
from pprint import pprint
import graph_dict


def has_cycle(graph: Dict[str, List[str]]) -> bool:
    """check if there is a cycle in the graph
    """
    if len(graph) == 0:
        return False

    # get a node from graph (randomly)
    start_node = list(graph.keys())[0]

    visited = {start_node}
    stack = [start_node]
    while len(stack) > 0:
        from_node = stack.pop(0)
        for to_node in graph[from_node]:
            if to_node not in visited:
                visited.add(to_node)
                stack.append(to_node)
            else:
                # we are visiting a visited node
                return True

    return False


if __name__ == '__main__':
    graph = {}
    graph_dict.link(graph, 'A', 'B')
    graph_dict.link(graph, 'B', 'C')
    pprint(graph)
    print('has cycle:', has_cycle(graph))

    graph_dict.link(graph, 'A', 'C')
    pprint(graph)
    print('has cycle:', has_cycle(graph))
