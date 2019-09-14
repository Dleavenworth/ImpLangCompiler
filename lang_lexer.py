import lexer

IDENTIFIER = 'IDENTIFIER'
NUMBER = 'NUMBER'
PUNCTUATION = 'PUNCTUATION'

token_list = [
    (r'[\n\t]+', None),
    (r'#[^\n]*', None),
    (r'[A-Za-z][A-Za-z0-9_]*', IDENTIFIER),
    (r'[0-9]+', NUMBER),
    (r'\t | \- | \* | \ | \(| \)', PUNCTUATION)
]


def lang_lexer(characters):
    return lexer.lexer(token_list, characters)
