class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        f={}
        for i in range(len(knowledge)):
            f[knowledge[i][0]]=knowledge[i][1]
        ans=""
        i=0
        while i<len(s):
            if s[i]=="(":
                i+=1
                key=""
                while s[i]!=")":
                    key+=s[i]
                    i+=1
                if key in f:
                    ans+=f[key]
                else:
                    ans+="?"
                i+=1
            else:
                ans+=s[i]
                i+=1
        return ans

                

        