from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        for r in d:
            if d[r] == 1:
                return r