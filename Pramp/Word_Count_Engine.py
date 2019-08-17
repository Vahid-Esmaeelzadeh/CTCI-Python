'''
Word Count Engine
'''


def word_count_engine1(document: str):
    table = {}  # (word, occurrence)
    temp = []

    maximum_occurrence = 0

    for c in document:
        if c.isalpha() or c == "'":
            temp.append(c.lower())

        if c.isspace():
            if len(temp) != 0:
                table[''.join(temp)] = table.get(''.join(temp), 0) + 1
                maximum_occurrence = max(table[''.join(temp)], maximum_occurrence)
                temp = []

    if len(temp) > 0:
        table[''.join(temp)] = table.get(''.join(temp), 0) + 1
        maximum_occurrence = max(table[''.join(temp)], maximum_occurrence)

    result = [[] for _ in range(maximum_occurrence)]

    for x in table:
        result[table[x]-1].append(x)

    final_res = []
    for i in range(len(result)-1, -1, -1):
        for x in result[i]:
            final_res.append([x, str(table[x])])

    return final_res




#print(word_count_engine1("Vahid Esmaeelzadeh'll be a young millionaire millionaire."))
#print(word_count_engine1("Practice makes perfect, you'll get perfecT by practice. just practice! just just just!!"))
print(word_count_engine1("Cause I'm Slim Shady, yes I'm the real Shady, All you other Slim Shadys are just imitating So won't the real Slim Shady, please stand up, Please stand up, Please stand up"))
