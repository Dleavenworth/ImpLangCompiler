# David Leavenworth III
# Phase 2.2
# This is the actual parser, it has one function for each 'noun' in the grammar, they're all mutually recursive
# They each return a node, and when all the functions fall out they'll have created a tree with the nodes in ast.py

import ast
import util


class Parser(object):
    def __init__(self, token_list, file):
        self.raw, self.tokens = util.generate_lists(token_list)
        self.counter = 0
        self.current_token = self.tokens[self.counter]
        self.current_raw = self.raw[self.counter]
        self.file = file

    def parse(self):
        return self.parse_expression()

    def error(self):
        self.file.write("Syntax error at token: " + self.current_raw + "\n")
        self.file.close()
        raise SystemExit(0)

    def consume_token(self):
        self.counter += 1
        if self.counter < len(self.tokens):
            self.current_token = self.tokens[self.counter]
            self.current_raw = self.raw[self.counter]
        else:
            pass

    def parse_statement(self):
        node = self.parse_base_statement()
        while self.current_raw is ';':
            self.consume_token()
            rhs = self.parse_base_statement()
            node = ast.BinaryOperator(node, ';', rhs, 'PUNCTUATION')
        return node

    def parse_base_statement(self):
        if self.current_token is 'IDENTIFIER':
            lhs = ast.LeafNode("IDENTIFIER", self.current_raw)
            self.consume_token()
            if self.current_raw == ":=":
                self.consume_token()
                return self.parse_assignment(lhs)
        if self.current_raw == 'if':
            self.consume_token()
            node = self.parse_if_statement()
            return node
        if self.current_raw == 'while':
            self.consume_token()
            node = self.parse_while_statement()
            return node
        if self.current_raw == 'skip':
            self.consume_token()
            node = ast.LeafNode('KEYWORD', self.current_raw)
            return node
        self.error()

    def parse_assignment(self, lhs):
        rhs = self.parse_expression()
        node = ast.BinaryOperator(lhs, ':=', rhs, 'PUNCTUATION')
        return node

    def parse_if_statement(self):
        predicate = self.parse_expression()
        if self.current_raw == "then":
            self.consume_token()
            true_state = self.parse_statement()
            if self.current_raw == "else":
                self.consume_token()
                false_state = self.parse_statement()
                if self.current_raw == "endif":
                    self.consume_token()
                    node = ast.TernaryOperator(predicate, true_state, false_state, 'if', 'KEYWORD')
                    return node
        self.error()

    def parse_while_statement(self):
        predicate = self.parse_expression()
        if self.current_raw == "do":
            self.consume_token()
            loop_state = self.parse_statement()
            self.consume_token()
            if self.current_raw == "endwhile":
                node = ast.BinaryOperator(predicate, 'while', loop_state, 'KEYWORD')
                self.consume_token()
                return node
        self.error()

    def parse_element(self):
        if self.current_raw is '(':
            self.consume_token()
            node = self.parse_expression()
            if self.current_raw is ')':
                self.consume_token()
                return node
        if self.current_token is 'IDENTIFIER':
            node = ast.LeafNode(self.current_raw, self.current_token)
            self.consume_token()
            return node
        if self.current_token is 'NUMBER':
            node = ast.LeafNode(self.current_raw, self.current_token)
            self.consume_token()
            return node
        self.error()

    def parse_piece(self):
        node = self.parse_element()
        while self.current_raw is '*':
            self.consume_token()
            node = ast.BinaryOperator(node, '*', self.parse_element(), 'PUNCTUATION')
        return node

    def parse_factor(self):
        node = self.parse_piece()
        while self.current_raw is '/':
            self.consume_token()
            node = ast.BinaryOperator(node, '/', self.parse_piece(), 'PUNCTUATION')
        return node

    def parse_term(self):
        node = self.parse_factor()
        while self.current_raw is '-':
            self.consume_token()
            node = ast.BinaryOperator(node, '-', self.parse_factor(), 'PUNCTUATION')
        return node

    def parse_expression(self):
        node = self.parse_term()
        while self.current_raw is '+':
            self.consume_token()
            node = ast.BinaryOperator(node, '+', self.parse_term(), 'PUNCTUATION')
        return node
