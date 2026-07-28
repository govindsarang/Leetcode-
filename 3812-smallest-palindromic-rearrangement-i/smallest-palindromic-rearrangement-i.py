from collections import Counter
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        #left half +(middle)+left half reverse
        n=len(s)
        leftlen=n//2
        lefthalf=list(s[:leftlen])
        lefthalf.sort()
        lefthalf="".join(lefthalf)
        if n%2==0:
            return lefthalf+lefthalf[::-1]
        else:
            return lefthalf+s[leftlen]+lefthalf[::-1]     
        """
        count=Counter(s)
        left=[]
        middle=""
        for ch in count:
            if count[ch]%2==1:
                middle=ch
            left.extend([ch]*(count[ch]//2))
        left.sort()
        left="".join(left)
        return left+middle+left[::-1]   
        """     