def numeric_formatter(*template):
    string = template[0]
    chars = "1234567890"
    if len(template) > 1:
        chars = template[1]

    cur = 0
    base = len(chars)
    nums = str()
    for s in string:
        if s.isalpha():
            nums += chars[cur]
            cur += 1
            if cur >= base:
                cur = 0
        else:
            nums += s

    return nums