class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        oddsum=0
        evensum=0
        i=1
        counto=0
        while True:
            if counto==n:
                break
            oddsum+=i
            counto+=1
            i+=2
        j=2
        counte=0
        while True:
            if counte==n:
                break
            evensum+=j
            counte+=1
            j+=2
        return gcd(oddsum,evensum)
            


        

        