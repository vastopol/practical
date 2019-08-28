def duplicate_encode(word):
    hashed = dict()
    stringed = str()
    word = word.upper()  # ignore case
    for w in word:
        if w not in hashed:
            hashed[w] = 1
        else:
            hashed[w] += 1
    for w in word:
        if hashed[w] == 1:
            stringed += '('
        else:
            stringed += ')'
    return stringed
