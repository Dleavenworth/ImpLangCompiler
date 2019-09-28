# David Leavenworth III
# Phase 1.2
# This is a helper function which just prints out the console output


def token_writer(output_file, token_list):
    for line_tuple in token_list:
        raw, tokens = line_tuple
        output_file.write("LINE: " + raw + '\n')
        for token in tokens:
            text, tag = token
            if tag is not 'FAIL':
                output_file.write(text + ' : ' + tag)
            else:
                output_file.write("ERROR READING" + ' "' + text + '"')
            output_file.write("\n")
        output_file.write("\n")
