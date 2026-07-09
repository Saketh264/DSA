class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        ans=""
        for p in permutations(arr):
            hour=p[0]*10+p[1]
            minutes=p[2]*10+p[3]
            if hour<24 and minutes<60:
                curr=f"{hour:02d}:{minutes:02d}"
                ans=max(ans,curr)
        return ans
        
            