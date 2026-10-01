class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        prefix=strs[0]
        s1=""
        for s in strs:
            i=0
            while i<len(s)and i<len(prefix):
                if s[i]==prefix[i]:
                    i+=1
                else:
                    break 
            prefix=prefix[:i]
        return prefix
        """
        for i in range(len(strs[0])):
            for j in range(1,len(strs)):
                if i>=len(strs[j]) or strs[j][i]!=strs[0][i]:
                    return strs[0][:i]
        return strs[0]

                

        
        


            






        
            



        