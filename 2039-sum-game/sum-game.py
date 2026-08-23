class Solution:
    def sumGame(self, num: str) -> bool:
        n=len(num)
        left=num[:n//2]
        right=num[n//2:]
        leftsum=0
        rightsum=0
        for i in range(len(left)):
            if left[i]!="?":
                leftsum+=int(left[i])
        for i in range(len(right)):
            if right[i]!="?":
                rightsum+=int(right[i])
        leftq=left.count("?")
        rightq=right.count("?")
        if (leftq+rightq)%2==1:
            return True
        if leftsum-rightsum!=9*(rightq-leftq)//2:
            return True
        return False


        
        
        