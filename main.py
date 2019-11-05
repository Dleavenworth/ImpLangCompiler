# David Leavenworth III
# Phase 2.2
# This is the test driver code for the lexer/parser

import sys

import scanner
import token_writer
import util
from Parser import Parser


def main():
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
        util.pre_ord(tree, f)


if __name__ == '__main__':
    main()
