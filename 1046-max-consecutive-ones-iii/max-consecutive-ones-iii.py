class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l,r,zeros,maxlen=0,0,0,0
        while r<=len(nums)-1:
            if nums[r]==0:zeros+=1
            while zeros>k:
                if nums[l]==0:
                    zeros-=1
                l+=1
            if zeros<=k:
                lens=r-l+1
                maxlen=max(maxlen,lens)
            r+=1
        return maxlen



