class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        mini,maxi=min(nums),max(nums)
        for i in nums: 
            if i!=mini and i!=maxi:
                return i
        return -1
