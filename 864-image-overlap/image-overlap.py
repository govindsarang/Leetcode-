class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:

        ones1=[]
        ones2=[]
        for i in range(len(img1)):
            for j in range(len(img1)):
                if img1[i][j]==1:
                    ones1.append((i,j))
                if img2[i][j]==1:
                    ones2.append((i,j))
        f={}
        for x1,y1 in ones1:
            for x2,y2 in ones2:
                dx=x2-x1
                dy=y2-y1
                if (dx,dy) in f:
                    f[(dx,dy)]+=1
                else:
                    f[(dx,dy)]=1
        return max(f.values(),default=0)
            

