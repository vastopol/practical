class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        nums = dict()
        size = len(A)//2
        for a in A:
            if a not in nums:
                nums[a] = 1
            else:
                nums[a] += 1
        for n in nums:
            if nums[n] == size:
                return n