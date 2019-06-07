def PalinPermutatoin(str):
    letters = [False] * 128

    for c in str:
        if c != ' ':
            letters[ord(c.lower())] ^= True

    odd_letters_count = 0

    for b in letters:
        if b is True:
            odd_letters_count += 1
        if odd_letters_count > 1:
            return False

    return True

def PalinPermutatoin_bit(str):

    letters = 0
    for c in str:
        if c != ' ':
            index = 1 << ord(c.lower()) - ord('a')
            letters ^= index

    if letters == 0:
        return True
    if (letters - 1) & letters == 0:
        return True

    return False

print(PalinPermutatoin('Vahid vhdidd'))

print(PalinPermutatoin_bit('vahid dihav'))
