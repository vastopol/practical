from collections import defaultdict

# given a string return the longest repeated substring
def longestRepSubstr(string: str): -> str
    # generate and count substrings
    substrs = defaultdict(int)             # substr -> frequency
    for t in range(len(string)):           # 0 to n-1
        for s in range(t+1, len(string)):  # t+1 to n-1
            tmp = string[t:s]
            substrs[tmp] += 1
    # find longest substring with highest frequency
    maximum = 0
    longest = str()
    for k in substrs:
        if substrs[k] > 1:          # check duplicates
            if len(k) > maximum:    # check length
                maximum = len(k)
                longest = k
    return longest