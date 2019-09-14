# David Leavenworth III
# Phase 1.1

import lexer


def scan_buffer(characters):
    line_results = []
    for line in characters.splitlines():
        line_results.append((line, (lexer.lexer(line))))
    return line_results
