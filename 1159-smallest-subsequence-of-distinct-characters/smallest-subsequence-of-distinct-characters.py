class Solution:
    def smallestSubsequence(self, s: str) -> str:
        f={}
        stack=[]
        seen=set()
        for i in s:
            if i in f:
                f[i]+=1
            else:
                f[i]=1
        for ch in s:
            f[ch]-=1
            if ch in seen:
                continue
            while stack and stack[-1]>ch and f[stack[-1]]>0:
                removed=stack.pop()
                seen.remove(removed)
            stack.append(ch)
            seen.add(ch)
        return "".join(stack)


        