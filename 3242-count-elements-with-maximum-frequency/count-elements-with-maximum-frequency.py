class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c=Counter(nums)
        vals=max(c.values())
        ans=0
        for i in c:
            if c[i]==vals: ans+=vals
        return ans
