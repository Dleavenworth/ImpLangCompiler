# David Leavenworth III
# Phase 2.1
# Credit to Jay Conrod for inspiration: http://jayconrod.com/posts/37/a-simple-interpreter-from-scratch-in-python--part-1-
# This file is the actual scanner, this is where the regex matches everything, it also returns the final list of tokens

import re
import token_definitions


def lexer(characters):
    token_definitions_list = token_definitions.token_list
    tokens = []
    position = 0
    got_match = False
    while position < len(characters) and not got_match:
        for token_definition in token_definitions_list:
            match = None
            regex_pattern, tag = token_definition
            regex = re.compile(regex_pattern)
            match = regex.match(characters, position)
            if match:
                got_match = True
                text = match.group(0)
                if tag is not 'IGNORE':
                    token = (text, tag)
                    tokens.append(token)
                position = match.end(0)
        if not got_match:
            tokens.append((characters[position], 'FAIL'))
            break
        got_match = False
    return tokens
