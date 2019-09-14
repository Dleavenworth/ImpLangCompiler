import sys
import lang_lexer


if __name__ == '__main__':
    # file_name = sys.argv[1]
    # print(file_name)
    with open("main.imp") as f:
        characters = f.read()
    tokens = lang_lexer.lang_lexer(characters)
    print ("done")

