class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        
        for i,v in enumerate(nums) :
            if i == sum(int(digit) for digit in str(abs(v))):
                return i
                
        return -1