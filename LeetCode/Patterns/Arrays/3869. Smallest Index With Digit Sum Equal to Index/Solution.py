class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        
        for i in nums :
            if nums.index(i) == sum(int(digit) for digit in str(abs(i))):
                return nums.index(i)
        return -1