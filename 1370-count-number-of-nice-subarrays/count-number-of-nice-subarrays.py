class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def array(nums,k):
            if k<0: return 0
            sums,l,r,c=0,0,0,0
            n=len(nums)
            while r<n:
                sums+=(nums[r])%2
                while sums>k:
                    sums-=(nums[l])%2
                    l+=1
                c+=(r-l+1)
                r+=1
            return c
        return array(nums,k)-array(nums,k-1)