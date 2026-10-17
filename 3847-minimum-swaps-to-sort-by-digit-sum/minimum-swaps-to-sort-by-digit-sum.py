class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        arr=[]
        for i in range(len(nums)):
            s=sum(map(int,str(nums[i])))
            arr.append((s, nums[i], i))
        arr.sort()
        visited = [False] * len(arr)
        swaps = 0
        for i in range(len(arr)):
            if visited[i] or arr[i][2] == i:
                continue
            cycle_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = arr[j][2]
                cycle_size += 1
            swaps += cycle_size - 1
        return swaps
        


        