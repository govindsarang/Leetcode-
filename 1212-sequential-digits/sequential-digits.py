class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans=[]
        digits="123456789"
        min_len=len(str(low))
        max_len=len(str(high))
        for length in range(min_len,max_len+1):
            for i in range(10-length):
                substring=digits[i:i+length]
                if low<=int(substring)<=high:
                    ans.append(int(substring))
        return ans
        