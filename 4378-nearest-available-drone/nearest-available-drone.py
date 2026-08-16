class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        mini=float('inf')
        ans=-1
        for i,(x,y,r) in enumerate(drones):
            val=abs(x-target[0])+abs(y-target[1])
            if val<=r:
                if val<mini:
                    mini=val
                    ans=i
        return ans
                

