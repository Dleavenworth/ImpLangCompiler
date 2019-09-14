import lexer

IDENTIFIER = 'IDENTIFIER'
NUMBER = 'NUMBER'
PUNCTUATION = 'PUNCTUATION'
IGNORE = 'IGNORE'

token_list = [
    (r'[\n|\t]+', IGNORE),
    (r'#[^\n]*', IGNORE),
    (r'\t|\-|\*|\|\(| \)', PUNCTUATION),
    (r'[0-9]+', NUMBER),
    (r'([a-z]|[A-Z])([a-z]|[A-Z]|[0-9])*', IDENTIFIER),
]


def lang_lexer(characters):
    return lexer.lexer(token_list, characters)
