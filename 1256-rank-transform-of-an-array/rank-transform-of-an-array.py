class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        f={}
        nums=sorted(set(arr))#to remove the duplicate values
        for i,num in enumerate(nums):
            f[num]=i+1 #to rank the elements accordingly
        for i in range(len(arr)):
            arr[i]=f[arr[i]]#to replace the elements with their ranks from the orginal array
        return arr
        
        