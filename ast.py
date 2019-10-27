
class AST(object):
    def pre_ord(self, root, token_type, depth=0, indent=4):
        if root:
            print(root.token) #+ " : " + token_type[depth+1])
            if isinstance(root, BinaryOperator):
                self.pre_ord(root.left, token_type, depth+1, indent)
                self.pre_ord(root.right, token_type, depth+1, indent)


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
