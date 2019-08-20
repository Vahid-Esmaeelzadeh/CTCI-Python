'''
Bracket Match (minimum number of brackets needed to add (at first/end of text) to the input to make it matched)

A string of brackets is considered correctly matched if every opening bracket in the string can be paired up with a
later closing bracket, and vice versa. For instance, “(())()” is correctly matched, whereas “)(“ and “((” aren’t.
For instance, “((” could become correctly matched by adding two closing brackets at the end, so you’d return 2.


Given a string that consists of brackets, write a function bracketMatch that takes a bracket string as an input
 and returns the minimum number of brackets you’d need to add to the input in order to make it correctly matched.

Examples:

input:  text = “(()”
output: 1

input:  text = “(())”
output: 0

input:  text = “())(”
output: 2
'''


def bracket_match(text):
    res = 0
    counter = 0

    for x in text:
        if x == '(':
            counter += 1

        if x == ')':
            counter -= 1
            if counter == -1:
                res += 1
                counter = 0

    return counter + res
