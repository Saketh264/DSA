class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        preMax=[0]*n
        sufMin=[0]*n
        preMax[0]=nums[0]
        for i in range(1,n):
            preMax[i]=max(preMax[i-1],nums[i])
        sufMin[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            sufMin[i]=min(sufMin[i+1],nums[i])
        for i in range(n):
            if preMax[i]-sufMin[i]<=k:
                return i
        return -1