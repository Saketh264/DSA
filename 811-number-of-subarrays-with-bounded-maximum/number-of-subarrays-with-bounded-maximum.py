class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        ans = 0
        last_invalid=-1
        last_valid=-1
        for i in range(len(nums)):
            if nums[i]>right:
                last_invalid=i
            if nums[i]>=left:
                last_valid=i
            ans+=last_valid-last_invalid
        return ans