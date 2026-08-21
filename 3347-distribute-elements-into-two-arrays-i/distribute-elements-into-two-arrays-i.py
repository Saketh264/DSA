class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1=[nums[0]]
        arr2=[nums[1]]
        op=nums[::-1]
        op.pop()
        op.pop()
        while op:
            if arr1[-1]>arr2[-1]:
                arr1.append(op.pop())
            else:
                arr2.append(op.pop())
        return arr1+arr2