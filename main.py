# David Leavenworth III
# Phase 1.1


import sys
import token_writer
import scanner

if __name__ == '__main__':
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    file = open(in_file)
    characters = file.read()
    file.close()
    line_results = scanner.scan_buffer(characters)
    with open(out_file, 'w') as f:
        token_writer.token_writer(f, line_results)
