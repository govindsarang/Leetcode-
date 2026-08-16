class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        c=[0,0,0]
        for i in stones:
            c[i%3]+=1
        zero=c[0]
        one=c[1]
        two=c[2]
        if one==0 or two == 0:
            return max(one, two) > 2 and zero % 2 == 1
        return abs(one - two) > 2 or zero % 2 == 0

