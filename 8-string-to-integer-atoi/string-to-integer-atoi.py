class Solution:
    def myAtoi(self, s: str) -> int:
        positive=True
        s=s.strip()
        num=0
        if len(s)==0:
            return 0
        if s[0]=="-":
            positive=False
            s=s[1:]
        elif s[0]=="+":
            s=s[1:]    
        for i in range(len(s)):
            if s[i].isdigit():
                digit=ord(s[i])-ord('0')
                num=num*10+digit
            else:
                break
        if positive==False:
            num=-num
        if num > 2147483647:
            return 2147483647

        if num < -2147483648:
            return -2147483648
        return num
#bookmarked to go through and revise  how to convert string to integer without using int () function (PYTHON)
        


        

        