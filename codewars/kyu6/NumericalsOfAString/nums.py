def numericals(ss):
    cnt = dict()
    num = str()
    for s in ss:
        if s not in cnt:
            cnt[s] = 1
            num += '1'
        else:
            cnt[s] += 1
            num += str(cnt[s])
    return num