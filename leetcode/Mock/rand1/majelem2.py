# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
# Note: The algorithm should run in linear time and in O(1) space.

# linear runtime, not even close to O(1) space though...

import math
from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hh = defaultdict(int)
        i = math.floor(len(nums)/3)
        l = list()
        for n in nums:
            hh[n] += 1
        for h in hh:
            if hh[h] > i:
                l.append(h)
        return l