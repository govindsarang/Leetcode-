class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            s=str(n)
            p=1
            for i in range(len(s)):
                p*=int(s[i])
            if p%t==0:
                return n
            n+=1
                

    
        