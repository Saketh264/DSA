class Solution:
    def reverseDegree(self, s: str) -> int:
        sums=0
        for i,val in enumerate(s):
            sums+=(26-(ord(val)-ord('a')))*(i+1)
        return sums