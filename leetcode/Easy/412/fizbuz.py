class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l = list()
        s = str()
        for x in range(1,n+1):
            s = str(x)
            if x % 3 == 0:
                s = "Fizz"
            if x % 5 == 0:
                s = "Buzz"
            if x % 15 == 0:
                s = "FizzBuzz"
            l.append(s)
        return l