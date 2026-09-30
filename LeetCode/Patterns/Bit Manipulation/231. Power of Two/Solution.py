class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if ( n**0.5 )% 1 == 0:
            return True
        else:return False