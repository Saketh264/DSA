class Solution:
    def findGCD(self, nums: List[int]) -> int:
        one=min(nums)
        two=max(nums)
        ans=1
        for i in range(1,two+1):
            if two%i==0 and one%i==0:
                ans=i
        return ans