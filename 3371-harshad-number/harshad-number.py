class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sums=0
        n=x
        while x>0:
            sums+=(x%10)
            x//=10
        if n%sums==0: return sums
        return -1