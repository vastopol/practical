import numpy as np
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        B = np.matrix(A)
        B = np.fliplr(B)  # reverse over x
        C = 1 - B         # zeros to ones
        return C.tolist()
    