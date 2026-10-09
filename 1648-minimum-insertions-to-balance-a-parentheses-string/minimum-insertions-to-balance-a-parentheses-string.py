class Solution:
    def minInsertions(self, s: str) -> int:
        res=0
        stack=[]
        i=0
        while i<len(s):
            if s[i]=="(":
                stack.append(s[i])
                i+=1
            else:
                if i+1<len(s) and s[i+1]==")":
                    i+=2
                else:
                    res+=1
                    i+=1
                if stack:
                    stack.pop()
                else:
                    res+=1
        res+=2*len(stack)
        return res

        