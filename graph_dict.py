#
# Graph structure can be easily represented by a dict. 
# We will show how to use dict to store a graph and a DFS (Depth First Search) algorithm
#
from typing import Dict, Set

def add_node(graph: Dict[str, Set[str]], node: str):
    """Add a new node to a graph"""
    if node not in graph:
        graph[node] = set()


def link(graph: Dict[str, Set[str]], from_node: str, to_node: str):
    """Link two nodes in graph"""
    add_node(graph, from_node)
    add_node(graph, to_node)
    graph[from_node].add(to_node)


def dfs(graph: Dict[str, Set[str]], start_node: str):
    """Travel on the graph using DFS algorithm"""
    if start_node not in graph:
        return

    visited = {start_node}
    stack = [start_node]
    while len(stack) > 0:
        from_node = stack.pop(0)
        for to_node in graph[from_node]:
            if to_node not in visited:
                print('From {} to {}'.format(from_node, to_node))
                visited.add(to_node)
                stack.append(to_node)


if __name__ == '__main__':
    graph = {}
    link(graph, 'A', 'B')
    link(graph, 'A', 'C')
    link(graph, 'B', 'D')
    link(graph, 'C', 'D')
    link(graph, 'D', 'E')

    dfs(graph, 'A')
