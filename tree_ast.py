#
# An abstract syntax tree. It is the result of parsing source code. 
# This also shows how to evaluate the tree to get the result of source code.
#
from typing import Callable, List


class ASTFuncNode(object):

    def __init__(self, evaluate_func: Callable[[List[object]], object]):
        self.evaluate_func = evaluate_func
        self.children = []

    def evaluate(self):
        args = [c.evaluate() for c in self.children]
        return self.evaluate_func(args)


class ASTValueNode(object):

    def __init__(self, value: object):
        self.value = value

    def evaluate(self):
        return self.value


def add(args: List[object]) -> object:
    return args[0] + args[1]


def sub(args: List[object]) -> object:
    return args[0] - args[1]


def mul(args: List[object]) -> object:
    return args[0] * args[1]


def div(args: List[object]) -> object:
    return args[0] / args[1]


def negetive(args: List[object]) -> object:
    return -args[0]


if __name__ == '__main__':
    # parsing -((1 + 2) / 3 * 4)
    # this is done by a compiler or interpreter automatically

    # nodes
    neg_node = ASTFuncNode(negetive)
    add_node = ASTFuncNode(add)
    div_node = ASTFuncNode(div)
    mul_node = ASTFuncNode(mul)

    node1 = ASTValueNode(1)
    node2 = ASTValueNode(2)
    node3 = ASTValueNode(3)
    node4 = ASTValueNode(4)

    # link them together
    add_node.children.append(node1)
    add_node.children.append(node2)
    div_node.children.append(add_node)
    div_node.children.append(node3)
    mul_node.children.append(div_node)
    mul_node.children.append(node4)
    neg_node.children.append(mul_node)

    # show the result
    print(neg_node.evaluate())
