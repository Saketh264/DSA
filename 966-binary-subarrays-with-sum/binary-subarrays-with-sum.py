class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def array(nums,goal):
            if goal<0: return 0
            sums,l,r,c=0,0,0,0
            n=len(nums)
            while r<n:
                sums+=nums[r]
                while sums>goal:
                    sums-=nums[l]
                    l+=1
                c+=(r-l+1)
                r+=1
            return c
        return array(nums,goal)-array(nums,goal-1)