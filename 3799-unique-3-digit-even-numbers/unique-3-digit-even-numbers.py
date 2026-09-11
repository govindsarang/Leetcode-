class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        f=[0]*10
        for d in digits:
            f[d]+=1
        count=0
        for h in range(1,10):
            if f[h]==0:
                continue
            f[h]-=1
            for t in range(0,10):
                if f[t]==0:
                    continue
                f[t]-=1
                for u in range(0,10,2):
                    if f[u]>0:
                        count+=1
                f[t]+=1
            f[h]+=1
        return count
            
            

        
            
        
        