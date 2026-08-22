class Solution:
    def checkDivisibility(self, n: int) -> bool:
        num=n
        s=0
        p=1
        while num!=0:
            digit=num%10
            s+=digit
            p*=digit
            num=num//10
        if n%(s+p)==0:
            return True
        return False
            