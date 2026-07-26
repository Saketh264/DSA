class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        tot=a+b+c
        return min(tot//2,tot-max(a,b,c))