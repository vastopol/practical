
# Take the difference by positions
# scale each part of the ip position by 256*[3,2,1,0]
def ips_between(start, end):
    s = start.split('.')
    e = end.split('.')
    f = [int(e[i]) - int(s[i]) for i in range(4)]
    g = [f[0]*(256**3) , f[1]*(256**2), f[2]*256, f[3]]
    h = sum(g)
    return h
