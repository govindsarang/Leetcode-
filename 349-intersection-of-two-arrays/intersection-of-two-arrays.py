class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        f1={}
        f2={}
        res=[]
        for i in nums1:
            if i in f1:
                f1[i]+=1
            else:
                f1[i]=1
        for i in nums2:
            if i in f2:
                f2[i]+=1
            else:
                f2[i]=1
        for i in f1:
            if (i in f1) and (i in f2):
                res.append(i)
        return list(set(res))
        """
        res=[]
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                res.append(nums1[i])
        return list(set(res))


        

        