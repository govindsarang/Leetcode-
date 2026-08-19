class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        f={}
        
        for key,value in reservedSeats:
            if key not in f:
                f[key]=[]
            f[key].append(value)
        con1=[2,3,4,5]
        con2=[4,5,6,7]
        con3=[6,7,8,9]
        count=(n-len(f))*2
        for i in f:
            seats=f[i]
            left=2 not in seats and 3 not in seats and 4 not in seats and 5 not in seats
            right=6 not in seats and 7 not in seats and 8 not in seats and 9 not in seats 
            middle=4 not in seats and 5 not in seats and 6 not in seats and 7 not in seats 
            if left and right:
                count+=2
            elif left or right or middle:
                count+=1
        return count

            




            

        