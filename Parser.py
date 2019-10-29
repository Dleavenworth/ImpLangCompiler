# David Leavenworth III
# Phase 2.1
# This is the actual parser, it has one function for each 'noun' in the grammar, they're all mutually recursive
# They each return a node, and when all the functions fall out they'll have created a tree with the nodes in ast.py

import ast


class Parser(object):
    def __init__(self, token_list):
        self.counter = 0
        self.raw, self.tokens = zip(*token_list[0])
        self.tokens = list(self.tokens)
        self.raw = list(self.raw)
        self.current_token = self.tokens[self.counter]
        self.current_raw = self.raw[self.counter]

    def parse(self):
        return self.parse_expression()

    def error(self):
        raise Exception("Invalid syntax")

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
            node = self.parse_base_statement()
        return node

    def parse_base_statement(self):
        if self.current_token is 'IDENTIFIER':
            self.consume_token()
            if self.current_raw is ':=':
                self.consume_token()
                node = self.parse_assignment()
                return node
        if self.current_raw is 'if':
            self.consume_token()
            node = self.parse_if_statement()
            return node
        if self.current_raw is 'while':
            self.consume_token()
            node = self.parse_while_statement()
            return node
        if self.current_raw is 'skip':
            node = ast.LeafNode('KEYWORD', self.current_raw)
            self.consume_token()
            pass
        self.error()

    def parse_assignment(self):
        node = ast.BinaryOperator(self.parse_element(), ':=', self.parse_expression(), 'PUNCTUATION')
        return node

    def parse_if_statement(self):
        node = ast.TerenaryOperator(self.parse_expression(), self.parse_statement(), self.parse_statement(), 'if', 'KEYWORD')
        return node

    def parse_while_statement(self):
        node = ast.BinaryOperator(self.parse_expression(), 'while', self.parse_statement(), 'KEYWORD')
        return node

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
