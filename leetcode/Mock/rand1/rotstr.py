# We are given two strings, A and B.
# A shift on A consists of taking string A and moving the leftmost character to the rightmost position.
# For example, if A = 'abcde', then it will be 'bcdea' after one shift on A.
# Return True if and only if A can become B after some number of shifts on A.

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if len(A) < 2:
            return True

        for i in range(1,len(A)+1):
            tmp = A[i:]
            j = 0
            while j < i:
                tmp += A[j]
                j += 1
            if tmp == B:
                return True
