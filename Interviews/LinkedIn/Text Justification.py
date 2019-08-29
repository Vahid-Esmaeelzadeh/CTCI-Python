'''
Text justification
'''


def fullJustify(words, max_width):
    if not words or not max_width:
        return None

    result = []
    text = ""
    next_text = ""

    # This loop will create line of words less than maxWidth and append in `lines` list
    words_num = len(words)
    for i in range(words_num):
        word = words[i]

        if len(text) == 0:
            next_text = word
        else:
            next_text = text + " " + word

        if len(next_text) > max_width:  # we have to add the current text to the result
            result.append(text)
            next_text = word  # we did not add this to the result yet
        if i == words_num - 1:  # we should add the next text in result
            result.append(next_text)

        text = next_text

    # Here we loop over the above build `lines` list and add spaces to adjust line length

    lines_num = len(result)

    for i in range(lines_num):
        line = result[i]
        len_line = len(line)
        count_spaces = line.count(" ")
        extra_spaces_needed = maxWidth - len_line
        # This is only for last line or line which has only one word
        if (extra_spaces_needed > 0 and count_spaces == 0) or (i == lines_num - 1):
            line += " " * extra_spaces_needed
        # Getting quotient and reminder to add more spaces between words
        elif extra_spaces_needed > 0 and count_spaces > 0:
            q, r = divmod(extra_spaces_needed, count_spaces)
            line = line.replace(" ", " " * (q + 1))
            if r > 0:
                line = line.replace(" ", " " * 2, r)
        result[i] = line

    return result


words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

print(fullJustify(words, maxWidth))