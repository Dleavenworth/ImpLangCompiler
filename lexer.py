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
                if tag:
                    token = (text, tag)
                    tokens.append(token)
                break
            if not match:
                return None
            else:
                position = match.end(0)
            return tokens
