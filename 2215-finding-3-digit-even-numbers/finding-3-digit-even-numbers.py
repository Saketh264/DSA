class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        op=[]
        for i in permutations(digits,3):
            a,b,c=i
            if a!=0 and c%2==0: op.append(int(str(a)+str(b)+str(c)))
        op=list(set(op))
        op.sort()
        return op