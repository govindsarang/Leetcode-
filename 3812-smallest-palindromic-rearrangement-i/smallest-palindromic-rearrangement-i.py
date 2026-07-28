from collections import Counter
class Solution:
    def smallestPalindrome(self, s: str) -> str:
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