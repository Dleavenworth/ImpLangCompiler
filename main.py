# David Leavenworth III
# Phase 2.2
# This is the test driver code for the lexer/parser

import sys

import scanner
import token_writer
import util
from Parser import Parser
from interpreter import Interpreter


def main():
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    file = open(in_file)
    characters = file.read()
    file.close()
    line_results = scanner.scan_buffer(characters)
    raw, parse_line = zip(*line_results)
    with open(out_file, 'w') as f:
        token_writer.token_writer(f, line_results)
        p = Parser(parse_line, f)
        tree = p.parse()
        util.pre_ord(tree, f)
        interp = Interpreter(tree, f)
        final = interp.fill_stack(tree)
        f.write("\nOutput: " + str(final[0][0]))


if __name__ == '__main__':
    main()
