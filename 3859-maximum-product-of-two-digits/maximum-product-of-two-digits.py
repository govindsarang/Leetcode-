class Solution:
    def maxProduct(self, n: int) -> int:
        arr=[]
        n=str(n)
        for i in range(len(n)):
            arr.append(int(n[i]))
        arr.sort()
        max1=arr[-1]
        max2=arr[-2]
        return max1*max2


        