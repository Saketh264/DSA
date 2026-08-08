class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        op=[]
        for a, b, c, d in permutations(words,4):
            if (a[0]==b[0] and a[3]==c[0] and d[0]==b[3] and d[3]==c[3]):
                op.append([a, b, c, d])
        return sorted(op)