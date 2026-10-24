class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        start=max(arriveAlice,arriveBob)
        end=min(leaveAlice,leaveBob)
        if start>end:
            return 0
        days=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def count(date):
            m=int(date[:2])
            d=int(date[3:])
            return sum(days[:m-1])+d
        return count(end)-count(start)+1
        