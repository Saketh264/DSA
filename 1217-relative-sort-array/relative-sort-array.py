from collections import defaultdict
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c=defaultdict(int)
        rem,res=[],[]
        for i in arr2:
            c[i]=0
        for i in arr1:
            if i in c:
                c[i]+=1
            else: rem.append(i)
        rem.sort()
        for i in arr2:
            res.extend([i]*c[i])
        res.extend(rem)
        return res