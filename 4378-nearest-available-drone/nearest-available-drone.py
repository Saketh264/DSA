class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        ans=-1
        mini=float('inf')
        for i in range(len(drones)):
            val=abs(drones[i][0]-target[0])+abs(drones[i][1]-target[1])
            if val<=drones[i][2] and val<mini:
                mini=val
                ans=i
        return ans
                

