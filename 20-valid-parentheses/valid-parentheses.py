class Solution:
    def isValid(self, s: str) -> bool:
        """
        stack=[]
        for i in s:
            if i==")":
                if stack and stack [-1]=="(":
                    stack.pop()
                else:
                    return False    
            elif i=="}":
                if stack  and stack [-1]=="{":#if stack checks if the stack is empty or not and stack[-1] checks whether the last element in the stack is the same bracket or not and applies for all the other if statements too
                    stack.pop()
                else:
                    return False 
            elif i=="]":
                if stack and stack [-1]=="[":
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i) #if it is not a closing bracket then append it to the stack 
        return len(stack)==0#using this because sometimes there might be only closing bracket in the input array ,then it should return fals at that times for ex:"(((" this should return false so this statement checks whether thr stack is empty or not at the end if it is empty then only it returns true 
        """
        stack=[]
        i=0
        while i<len(s):
            if s[i]==")":
                if stack and stack[-1]=="(":
                    stack.pop()
                else:
                    return False
            elif stack and  s[i]=="]":
                if stack[-1]=="[":
                    stack.pop()
                else:
                    return False
            elif s[i]=="}":
                if stack and  stack[-1]=="{":
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
            i+=1
        return len(stack)==0
                

            

            
        