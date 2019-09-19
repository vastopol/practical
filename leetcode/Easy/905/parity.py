class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even = sorted(filter(lambda x: (x%2)==0,A))
        odd  = sorted(filter(lambda x: x%2,A))
        return even + odd
        