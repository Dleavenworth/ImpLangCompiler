# David Leavenworth III
# Phase 3.1
# This is a helper function which just prints out the console output


def token_writer(output_file, token_list):
    output_file.write("TOKENS: \n")
    for line_tuple in token_list:
        raw, tokens = line_tuple
        output_file.write("LINE: " + raw + '\n')
        for token in tokens:
            text, tag = token
            if tag is not 'FAIL':
                output_file.write(text + ' : ' + tag)
            else:
                output_file.write("ERROR READING" + ' "' + text + '"')
                raise SystemExit(0)
            output_file.write("\n")
        output_file.write("\n")
