#
# Read graph data structure from a file where the first line in a block a from-node, and the following lines are the to-nodes. 
# Blocks are sperated by an empty line.
#
from typing import Dict, List, TextIO

def add_node(graph: Dict[str, List[str]], node: str):
    """ add a node to graph
    """
    if node not in graph:
        graph[node] = []


def read_graph(fin: TextIO) -> Dict[str, List[str]]:
    """ read a graph from file
    """
    graph = {}
    cur_node = None

    for line in fin.readlines():
        l = line.strip()
        if not cur_node:    # start line, from node
            cur_node = l
            add_node(graph, cur_node)
        else:
            if len(l) == 0: # empty line, new block
                cur_node = None
            else:           # to node
                if l not in graph[cur_node]:
                    graph[cur_node].append(l)

    return graph


if __name__ == '__main__':
    import pprint # pretty printer
    with open('graph.txt') as fin:
        graph = read_graph(fin)
        pprint.pprint(graph)
