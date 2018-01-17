#
# This is an example of how to evaluate expressions
#
   

class ExpNode(object):

    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right

    def _evaluate_child(self, child):
        if child:
            return child.evaluate()
        else:
            return None

    def evaluate(self):
        left_value = self._evaluate_child(self.left)
        right_value = self._evaluate_child(self.right)
        return self._eval(left_value, right_value)

    def _eval(self, left_value, right_value):
        raise NotImplementedError()

    def __str__(self):
        return '({} {} {})'.format(self.left, self.name, self.right)


class AddExpNode(ExpNode):

    def __init__(self, left, right):
        super().__init__('+', left, right)

    def _eval(self, left_value, right_value):
        return left_value + right_value


class SubExpNode(ExpNode):

    def __init__(self, left, right):
        super().__init__('-', left, right)

    def _eval(self, left_value, right_value):
        return left_value - right_value


class MulExpNode(ExpNode):

    def __init__(self, left, right):
        super().__init__('*', left, right)

    def _eval(self, left_value, right_value):
        return left_value * right_value


class DivExpNode(ExpNode):

    def __init__(self, left, right):
        super().__init__('/', left, right)

    def _eval(self, left_value, right_value):
        return left_value / right_value


class ValueNode(ExpNode):

    def __init__(self, value):
        super().__init__(str(value), None, None)

    def _eval(self, left_value, right_value):
        return float(self.name)

    def __str__(self):
        return self.name


if __name__ == '__main__':
    # parsed AST of (1 + 5 - 2) * 3 / 4
    add = AddExpNode(ValueNode(1), ValueNode(5))
    sub = SubExpNode(add, ValueNode(2))
    mul = MulExpNode(sub, ValueNode(3))
    root = DivExpNode(mul, ValueNode(4))

    print(root)
    print(root.evaluate())