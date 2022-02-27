# ImpLangInterpreter
## Overview
This is the repository for the ImpLang interpreter project I completed in my programing languages course during the fall semester of 2019. The grammar of the language is the below regex:

![image](https://user-images.githubusercontent.com/9221551/155898735-2a3b4cf2-180e-4858-93c5-bf95f32747c4.png)

This can also be found in token_definitions.py

To run:
``$ python main.py <input file> <output file>``

Where the input file is a program which follows the above grammar, and the output file is any .txt file.

There is an example input file provided in this repo, it is called main.imp. You can run the program with this file as the input file to see it at work.

This project was written in Python 3.x.

## Limitations
The parser module can recognize and create the abstract syntax tree for all keywords, however, the evalutaor is only able to evaluate arithmetic expressions with no keywords.
