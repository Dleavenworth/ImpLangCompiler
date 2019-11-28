# David Leavenworth III
# Phase 3.1
# This is the file that defines the tree as a class, each class underneath
# the AST base class will have subclasses Leaf, and Interior
# the InteriorNode subclass will have subclasses, BinaryOperator, and TernaryOperator, which will have 2 and 3 children
# respectively


class AST(object):
    pass


class InteriorNode(AST):
    def __init__(self, token_type):
        self.token_type = token_type


class LeafNode(AST):
    def __init__(self, token, token_type):
        self.token_type = token_type
        self.token = token


class BinaryOperator(InteriorNode):
    def __init__(self, left, token, right, token_type):
        super().__init__(token_type)
        self.left = left
        self.token = token
        self.right = right


class TernaryOperator(InteriorNode):
    def __init__(self, left, center, right, token, token_type):
        super().__init__(token_type)
        self.token = token
        self.left = left
        self.right = right
        self.center = center
