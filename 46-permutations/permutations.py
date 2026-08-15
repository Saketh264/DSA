class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        op=[]
        for i in permutations(nums):
            op.append(i)
        return op
        