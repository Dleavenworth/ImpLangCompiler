# David Leavenworth III
# Phase 1.2
# This is the test driver code for the lexer

import sys
import token_writer
import scanner
from Parser import *
import ast


if __name__ == '__main__':
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    file = open(in_file)
    characters = file.read()
    file.close()
    line_results = scanner.scan_buffer(characters)
    raw, parse_line = zip(*line_results)
    p = Parser(parse_line)
    tree = p.parse()
    with open(out_file, 'w') as f:
        token_writer.token_writer(f, line_results)
    ast.AST.pre_ord(tree, tree, p.tokens)
