class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        c={}
        rank=1
        for i in sorted(list(set(arr))):
            c[i]=rank
            rank+=1
        for i in range(len(arr)):
            arr[i]=c[arr[i]]
        return arr