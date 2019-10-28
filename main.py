# David Leavenworth III
# Phase 2.1
# This is the test driver code for the lexer/parser

import sys
import token_writer
import scanner
from parser import *
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
        ast.AST.pre_ord(tree, tree, f)
