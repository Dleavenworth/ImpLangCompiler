import ast


class Interpreter:
    def __init__(self, tree, file):
        self.tree = tree
        self.stack = []
        self.file = file

    def fill_stack(self, tree):
        if tree:
            self.stack.append((tree.token, tree.token_type))
            self.eval()
            if isinstance(tree, ast.TernaryOperator):
                self.fill_stack(tree.left)
                self.fill_stack(tree.center)
                self.fill_stack(tree.right)
            if isinstance(tree, ast.BinaryOperator):
                self.fill_stack(tree.left)
                self.fill_stack(tree.right)
        return self.stack

    def eval(self):
        while len(self.stack) >= 3:
            if self.stack[len(self.stack)-1][1] == "NUMBER":
                if self.stack[len(self.stack)-2][1] == "NUMBER":
                    if self.stack[len(self.stack)-3][1] == "PUNCTUATION":
                        self.resolve()
                    else:
                        break
                else:
                    break
            else:
                break

    def resolve(self):
        if self.stack[len(self.stack)-3][0] == '+':
            self.stack.append(self.add())
        elif self.stack[len(self.stack)-3][0] == '-':
            self.stack.append((self.sub()))
        elif self.stack[len(self.stack)-3][0] == '*':
            self.stack.append(self.mult())
        elif self.stack[len(self.stack)-3][0] == '/':
            self.stack.append(self.div())

    def add(self):
        num2 = self.stack.pop()
        num1 = self.stack.pop()
        self.stack.pop()
        ret = int(num1[0]) + int(num2[0])
        return ret, "NUMBER"

    def sub(self):
        num2 = self.stack.pop()
        num1 = self.stack.pop()
        self.stack.pop()
        ret = int(num1[0]) - int(num2[0])
        if ret < 0:
            ret = 0
        return ret, "NUMBER"

    def mult(self):
        num2 = self.stack.pop()
        num1 = self.stack.pop()
        self.stack.pop()
        ret = int(num1[0]) * int(num2[0])
        return ret, "NUMBER"

    def div(self):
        num2 = self.stack.pop()
        num1 = self.stack.pop()
        self.stack.pop()
        if num1[0] == "0" or num2[0] == "0":
            self.file.write("DIVIDE BY ZERO ERROR")
            self.file.close()
            raise SystemExit(0)
        ret = int(num1[0]) // int(num2[0])
        return ret, "NUMBER"
