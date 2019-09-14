import sys
import lang_lexer


if __name__ == '__main__':
    # file_name = sys.argv[1]
    # print(file_name)
    file = open("main.imp")
    characters = file.read()
    file.close()
    tokens = lang_lexer.lang_lexer(characters)
    for token in tokens:
        print (token)
