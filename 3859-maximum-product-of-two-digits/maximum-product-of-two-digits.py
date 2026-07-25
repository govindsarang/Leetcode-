class Solution:
    def maxProduct(self, n: int) -> int:
        arr=[]
        n=str(n)
        for i in range(len(n)):
            arr.append(int(n[i]))
        arr.sort()
        return arr[-1]*arr[-2]


        