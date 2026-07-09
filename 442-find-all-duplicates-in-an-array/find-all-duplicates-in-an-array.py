class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        c=Counter(nums)
        op=[]
        for key,value in c.items():
            if value==2:
                op.append(key)
        return op