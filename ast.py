# David Leavenworth III
# Phase 2.1
# This is the file that defines the tree as a class, each class underneath
# the AST base class will be a subclass, and a type of node in the tree
# There is also the pre-order traversal which prints the AST to the outfile, and does it nice and short with recursion

class AST(object):
    def pre_ord(self, root, file, depth=0):
        if depth is 0:
            file.write("AST: \n")
        if root:
            file.write(depth*" " + root.token + " : " + root.token_type + "\n")
            if isinstance(root, BinaryOperator):
                self.pre_ord(root.left, file, depth+4)
                self.pre_ord(root.right, file, depth+4)


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
