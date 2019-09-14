import lexer

IDENTIFIER = 'IDENTIFIER'
NUMBER = 'NUMBER'
PUNCTUATION = 'PUNCTUATION'

token_list = [
    [r'[\n\t]+', None],
    [r'#[^\n]*', None],
    [r'([a-z] | [A-Z]) | ([a-z] | [A-Z] | [0-9])*', IDENTIFIER],
    [r'([0-9]+', NUMBER],
    [r'\t | \- | \* | \ | \(| \)', PUNCTUATION]
]


def lang_lexer(characters):
    return lexer.lexer(token_list, characters)
