class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        f={}
        left=0
        maxi=0
        for right in range(len(s)):
            if s[right] in f:
                f[s[right]]+=1
            else:
                f[s[right]]=1
            while f[s[right]]>2:
                f[s[left]]-=1
                left+=1
            maxi=max(maxi,right-left+1)
        return maxi

