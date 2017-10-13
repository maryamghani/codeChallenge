"""
Suppose you are programming for a really old-school internet newspaper, one that is so
old-school that they only have monospace fonts. However,
the editor really wants to see the monospace text justified to fit into the
column space he has at a particular time. Your job is to write
a program that will take as input the width of the column in characters
and the entire text to be formatted, and return the same text except
justified to fit into the column. The last line does not have to be justified



For example, consider the following input:
***
20
The quick brown fox jumps over the lazy dog.
***

Then the output of your program should be:
***
The quick brown fox jumps over the lazy dog.
***
"""
import textwrap

# this question can get solve with Dynamic Programming as well.


def monospace(string):
    text = textwrap.dedent(string).strip()
    return textwrap.fill(text, width=20)

if __name__ == '__main__':
    s = 'The quick brown fox jumps over the lazy dog.'
    print(monospace(s))

