import sys
import lang_lexer


def main():
    characters = []
    with open(sys.argv[1]) as f:
        for line in f:
            characters.append(line)
    lang_lexer.lang_lexer(characters)
