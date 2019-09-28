# David Leavenworth III
# Phase 1.1

IDENTIFIER = 'IDENTIFIER'
NUMBER = 'NUMBER'
PUNCTUATION = 'PUNCTUATION'
IGNORE = 'IGNORE'
FAIL = 'FAIL'
KEYWORD = 'KEYWORD'

token_list = [
    (r'[\n\t ]+', IGNORE),
    # (r'#.*$', IGNORE), In case we want to handle comments later
    (r'(?:\+|\-|\*|\/|\(|\)|(:=)|(;))', PUNCTUATION),
    (r'[0-9]+', NUMBER),
    (r'(?:(if)|(then)|(else)|(endif)|(while)|(do)|(endwhile)|(skip))(?!\S)', KEYWORD),
    (r'([a-zA-Z])([a-zA-Z0-9])*', IDENTIFIER),
]
