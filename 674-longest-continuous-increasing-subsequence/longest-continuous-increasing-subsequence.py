class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        c,maxi=1,1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                c+=1
            else:
                c=1
            maxi=max(maxi,c)
        return maxi
        