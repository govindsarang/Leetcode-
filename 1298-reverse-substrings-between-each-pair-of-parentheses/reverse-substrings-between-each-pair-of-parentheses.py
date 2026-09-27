class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        for i in s:
            if i ==")":#if closed paranthesis occurs then reverse the words inside the closed paranthesis
                sub=[]#take a list
                while  stack and stack[-1]!="(":#the loop runs till open paranthesis arrives
                    sub.append(stack.pop()) #appending all the elements inside paranthesis in new list
                stack.pop()#removing (
                stack.extend(sub)   #adding the new list which gives reverse of the elements inside the paranthesis to the stack           
            else:#append until closed paranthesis reaches
                stack.append(i)
        return "".join(stack)

        