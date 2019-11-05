# David Leavenworth III
# Phase 2.2
# This is just a util file, which will contain all of the utility functions for the Parser module of this project

import ast


def flatten_list(input_list):
    flat_list = []
    for sublist in input_list:
        for item in sublist:
            flat_list.append(item)
    return flat_list


def generate_lists(input_list):
    token_list = list(input_list)
    raw = []
    tokens = []
    for i in token_list:
        if len(i) > 0:
            temp_raw, temp_tokens = zip(*i)
            raw.append(temp_raw)
            tokens.append(temp_tokens)
    raw = flatten_list(raw)
    tokens = flatten_list(tokens)
    return raw, tokens


def pre_ord(root, file, depth=0):
    if not file.closed:
        if depth is 0:
            file.write("AST: \n")
        if root:
            file.write(depth * " " + root.token + " : " + root.token_type + "\n")
            if isinstance(root, ast.TernaryOperator):
                pre_ord(root.left, file, depth + 4)
                pre_ord(root.center, file, depth + 4)
                pre_ord(root.right, file, depth + 4)
            if isinstance(root, ast.BinaryOperator):
                pre_ord(root.left, file, depth + 4)
                pre_ord(root.right, file, depth + 4)