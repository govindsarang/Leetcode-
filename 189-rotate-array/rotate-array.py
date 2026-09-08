class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l=len(nums)
        k=k%l#this is required when k value is more than the n or the length of the array , when array has one element and k =2 then k%n gives the reminder , during normal test case(when k<n) then doing '%' gives same array length back or gives same k value back 
        def reverse(left,right):#a function is used to reverse the array parts by parts
            while left<right:
                nums[left],nums[right]=nums[right],nums[left]#logic for reversing with 2 pointers
                left+=1#increementing left and right valuse adter wach iteration
                right-=1
        reverse(0,l-1)#reversing the whole array {1,2,3,4,5}={5,4,3,2,1} 
        reverse(0,k-1)#reversing the k index elements if k =3 {'3,4,5',2,1}
        reverse(k,l-1)#reversing the other elements or remaining elements=> {3,4,5,'1,2'}
        
        




            
            


                

        """
        Do not return anything, modify nums in-place instead.
        """
        