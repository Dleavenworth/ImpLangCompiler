
class AST(object):
    def __init__(self, root):
        self.root = root
        self.nodes = []


class BinaryOperator(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right


class Num(AST):
    def __init__(self, token):
        self.token = token


class Identifier(AST):
    def __init__(self, token):
        self.token = token
