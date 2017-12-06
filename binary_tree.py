#
# A Binary Tree. This example also shows how to use visitor pattern (in Python all you need is pass in a function).
#
from typing import Callable


class BinaryTreeNode(object):

    def __init__(self, value, left: 'BinaryTreeNode' = None, right: 'BinaryTreeNode' = None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


class BinaryTree(object):

    def __init__(self, root: BinaryTreeNode):
        self.root = root

    def dfs(self, visitor: Callable[[BinaryTreeNode], None]):
        stack = [self.root]
        while len(stack) > 0:
            cur = stack.pop()
            visitor(cur)

            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)

    def bfs(self, visitor: Callable[[BinaryTreeNode], None]):
        queue = [self.root]
        while len(queue) > 0:
            cur = queue.pop(0)
            visitor(cur)

            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)


if __name__ == '__main__':
    root = BinaryTreeNode('A')
    root.left = BinaryTreeNode('B')
    root.right = BinaryTreeNode('C')
    root.left.left = BinaryTreeNode('D')
    root.right.left = BinaryTreeNode('E')

    tree = BinaryTree(root)

    def visit_and_print(node: BinaryTreeNode):
        print('Visiting: {}'.format(node))

    print('DFS:')
    tree.dfs(visit_and_print)
    print('BFS:')
    tree.bfs(visit_and_print)
