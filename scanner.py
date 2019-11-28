# David Leavenworth III
# Phase 3.1
# This is a helper function to print out all of the lines to a console
# it just splits all of the lines into entries in the line_results list

import lexer


def scan_buffer(characters):
    line_results = []
    for line in characters.splitlines():
        line_results.append((line, (lexer.lexer(line))))
    return line_results
