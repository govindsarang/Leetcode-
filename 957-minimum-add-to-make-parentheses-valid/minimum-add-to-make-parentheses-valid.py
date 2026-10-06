class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opencount=0
        res=0
        for i in s:
            if i=="(":
                opencount+=1
            else:
                opencount-=1
                if opencount<0:
                    opencount=0
                    res+=1
                    
        return res+opencount
        