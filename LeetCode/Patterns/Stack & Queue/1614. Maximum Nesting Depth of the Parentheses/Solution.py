class Solution:
    def maxDepth(self, s: str) -> int:
        d=0 
        r=0
        for c in s:
            if c == ')':
                d -= 1 
                continue
            if c != '(':
                continue
            d+=1
            if d>r:
                r=d
        return r