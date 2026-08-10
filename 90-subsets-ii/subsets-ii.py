class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        def helper(ind,arr):
            res.append(arr.copy())
            for i in range(ind,len(nums)):
                if(i>ind and nums[i]==nums[i-1]):continue
                arr.append(nums[i])
                helper(i+1,arr)
                arr.pop() 
        helper(0,[])
        return res

        