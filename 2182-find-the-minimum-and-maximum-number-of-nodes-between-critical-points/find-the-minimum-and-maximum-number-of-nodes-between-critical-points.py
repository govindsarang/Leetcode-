# Definition for singly-linked list.
# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/$0class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
    #do this probelm by taking 3 pointers ,one which points to current node, one to previous and one to next just to check whether the current node is local maxima or local minima
        if head== None:
            return head
        curr=head.next#we are asssigning the curr,prev and next pointers 
        prev=head
        nex=head.next.next
        pos=2#starting from 2 as the first one does not have prev node so obivio its not a critical point
        arr=[]#appending all the positions of the critical points in an array
        while nex!=None:
            if curr.val>prev.val and curr.val>nex.val:#condition for local maxima
                arr.append(pos)
            if curr.val<prev.val and curr.val<nex.val:#condition for local minima
                arr.append(pos)
            #after appending traverse all the pointers and increement pos variable to point out to next node
            pos+=1
            prev=curr
            curr=curr.next
            nex=curr.next
        #edge case where if there are less than 2 critical points then -1
        if len(arr)<2:
            return [-1,-1]
        mindis=float('inf')
        #after having an array which coontains positions of all the criticcal points just find the min and max distance bt them
        for i in range(1,len(arr)):
            dis=arr[i]-arr[i-1]
            mindis=min(mindis,dis)#as the pos are sorted so the min dis will be b/t 2 consecutive critical points
        maxdis=arr[-1]-arr[0]#max will be the distance b/t first and last critical point 
        return [mindis,maxdis]





        