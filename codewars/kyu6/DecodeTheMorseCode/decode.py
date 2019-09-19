def decodeMorse(morse_code):
    mor = str()
    morse = list()
    for m in morse_code:
        if m != ' ':
            mor += m
        elif m == ' ':
            morse.append(mor)
            mor = str()
    if mor != str():  # in case no ' ' in string
        morse.append(mor)

    mor = str()
    boom = True
    for m in morse:
        if m == '':
            if not boom:
                mor += ' '
                boom = True
        else:
            boom = False
            mor += MORSE_CODE[m]
    if mor[-1] == ' ':  # in case last char is ' '
        mor = mor[:-1]

    return mor