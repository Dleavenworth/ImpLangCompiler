import re


def lexer(token_list, characters):
    tokens = []
    position = 0
    while position < len(characters):
        match = None
        for token_expr in token_list:
            regex_pattern, tag = token_expr
            regex = re.compile(regex_pattern)
            match = regex.match(characters, position)
            if match:
                text = match.group(0)
                if tag is not 'IGNORE':
                    token = (text, tag)
                    tokens.append(token)
                    position = match.end(0)
                else:
                    position = position+1
            if not match:
                if match is None:
                    position = position+1
                print("Does not match")
    return tokens
