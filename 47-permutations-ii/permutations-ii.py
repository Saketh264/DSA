class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        op=[]
        for i in permutations(nums):
            op.append(i)
        return list(set(op))