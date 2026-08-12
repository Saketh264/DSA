class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        op=[]
        for i in words:
            x=i.split(separator)
            for j in x:
                if j=="": continue
                op.append(j)
        return op
        