class Solution:
    def isThree(self, n: int) -> bool:
        vis=set()
        for i in range(1,int(n**0.5)+1):
            if n%i==0:
                vis.add(i)
                vis.add(n//i)
        # print(vis)
        return len(vis)==3