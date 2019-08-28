def add_letters(*letters):
    if   len(letters) == 0:
        return 'z'
    elif len(letters) == 1:
        return letters[0]
    acc = 0
    ascii = 96  # offet into ascii table
    alpha = 26  # mod base lowercase letters
    for letter in letters:
        # ascii 'a' = 97 and 'z' = 122
        num = ord(letter) - ascii
        acc += num
    if (acc % alpha) == 0:
        char = 122
    else:
        char = (acc % alpha) + ascii
    return chr(char)