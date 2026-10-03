class Solution:
    def countSegments(self, s: str) -> int:
        if len(s)==0:
            return 0
        word=""
        s+=" "
        res=[]
        for i in range(len(s)):
            if s[i]==" ":
                if word!="":
                    res.append(word)
                    word=""
            else:
                word+=s[i]
        return len(res)