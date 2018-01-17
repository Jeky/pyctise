#
# A builder to build AST from expression string using Shunting-yard algorithm (https://en.wikipedia.org/wiki/Shunting-yard_algorithm)
#

from cal_evaluator import *

OPERATORS = ['+', '-', '*', '/']
LEFT_BRACKET = '('
RIGHT_BRACKET = ')'
DIGITS = [str(i) for i in range(10)]
PRECEDENCES = {
    '+' : 0,
    '-' : 0,
    '*' : 1,
    '/' : 1,
    '(' : -1,
    ')' : 0
}


class Token(object):

    def __init__(self, value):
        self.value = value

    def is_op(self):
        return self.value in OPERATORS

    def is_digit(self):
        return self.value.isdigit()

    def is_LEFT_BRACKET(self):
        return self.value == LEFT_BRACKET

    def is_RIGHT_BRACKET(self):
        return self.value == RIGHT_BRACKET

    def __le__(self, other):
        if self.is_digit():
            return True
        else:
            return PRECEDENCES[self.value] <= PRECEDENCES[other.value]

    def __ge__(self, other):
        if self.is_digit():
            return True
        else:
            return PRECEDENCES[self.value] >= PRECEDENCES[other.value]

    def __str__(self):
        return self.value

    def __repr__(self):
        return str(self)

class ASTBuilder(object):

    def __init__(self):
        self.tokens = []
        self.operator_stack = []
        self.expr_stack = []

    def tokenize(self, expression):
        self.tokens = [Token(LEFT_BRACKET)]
        queue = list(expression)
        digit_buffer = ''

        while len(queue) > 0:
            c = queue.pop(0)
            if c in DIGITS:
                digit_buffer += c
            else:
                if len(c) > 0:
                    self.tokens.append(Token(digit_buffer))
                    digit_buffer = ''

                self.tokens.append(Token(c))

        if len(digit_buffer) > 0:
            self.tokens.append(Token(digit_buffer))

        self.tokens.append(Token(RIGHT_BRACKET))

    def build_ast(self, expression):
        self.tokenize(expression)
        self.operator_stack = []
        self.expr_stack = []

        while len(self.tokens) > 0:
            t = self.tokens.pop(0)
            if t.is_LEFT_BRACKET():
                self.operator_stack.append(t)
            elif t.is_digit():
                self.expr_stack.append(ValueNode(t.value))
            elif t.is_op():
                self.push_op(t)
                self.operator_stack.append(t)
            elif t.is_RIGHT_BRACKET():
                while len(self.operator_stack) > 0 and not self.operator_stack[-1].is_LEFT_BRACKET():
                    self.push_op(t)
                self.operator_stack.pop()

        return self.expr_stack.pop()

    def push_op(self, op):
        while len(self.operator_stack) > 0 and self.operator_stack[-1] >= op:
            op_token = self.operator_stack.pop()
            e2 = self.expr_stack.pop()
            e1 = self.expr_stack.pop()
            if op_token.value == '+':
                self.expr_stack.append(AddExpNode(e1, e2))
            elif op_token.value == '-':
                self.expr_stack.append(SubExpNode(e1, e2))
            elif op_token.value == '*':
                self.expr_stack.append(MulExpNode(e1, e2))
            elif op_token.value == '/':
                self.expr_stack.append(DivExpNode(e1, e2))

if __name__ == '__main__':
    exp = '(1+5-2)*3/4'
    root = ASTBuilder().build_ast(exp)

    print(root)
    print(root.evaluate())
