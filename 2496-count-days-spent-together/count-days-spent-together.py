class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        d={"01":31,"02":28,"03":31,"04":30,"05":31,"06":30,"07":31,"08":31,"09":30,"10":31,"11":30,"12":31
        }
        a=arriveAlice.split('-')
        b=leaveAlice.split('-')
        e=leaveBob.split('-')
        c=arriveBob.split('-')
        for i in range(1,int(a[0])):
            a[1]=str(int(a[1])+d[f"{i:02d}"])
        for i in range(1, int(b[0])):
            b[1]=str(int(b[1])+d[f"{i:02d}"])
        for i in range(1,int(c[0])):
            c[1]=str(int(c[1])+d[f"{i:02d}"])
        for i in range(1,int(e[0])):
            e[1]=str(int(e[1])+d[f"{i:02d}"])
        a=int(a[1])
        b=int(b[1])
        c=int(c[1])
        e=int(e[1])
        start=max(a,c)
        end=min(b,e)
        if start>end:
            return 0
        return end-start+1