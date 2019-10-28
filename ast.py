
class AST(object):
    def pre_ord(self, root, file, depth=0):
        if depth is 0:
            file.write("AST: \n")
        if root:
            file.write(depth*" " + root.token + " : " + root.token_type + "\n")
            if isinstance(root, BinaryOperator):
                self.pre_ord(root.left, file, depth+1)
                self.pre_ord(root.right, file, depth+1)


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
