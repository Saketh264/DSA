class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n=len(nums)
        if n<3: return len(set(nums))
        pair=set()
        for i in range(n):
            for j in range(i+1,n):
                pair.add(nums[i]^nums[j])
        ans=set()
        for x in pair:
            for j in nums:
                ans.add(x^j)
        return len(ans)