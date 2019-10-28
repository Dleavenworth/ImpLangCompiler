
class AST(object):
    def pre_ord(self, root, depth=0):
        if root:
            print(depth*" " + root.token + " : " + root.token_type)
            if isinstance(root, BinaryOperator):
                self.pre_ord(root.left, depth+1)
                self.pre_ord(root.right, depth+1)


class BinaryOperator(AST):
    def __init__(self, left, op, right, token_type='PUNCTUATION'):
        self.left = left
        self.token = self.op = op
        self.right = right
        self.token_type = token_type


class Num(AST):
    def __init__(self, token, token_type='NUMBER'):
        self.token = token
        self.token_type = token_type


class Identifier(AST):
    def __init__(self, token, token_type='IDENTIFIER'):
        self.token = token
        self.token_type = token_type
