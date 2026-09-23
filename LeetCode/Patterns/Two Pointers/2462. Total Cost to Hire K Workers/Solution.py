class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        ans = 0 
        while k != 0 :
            ans = ans + min(costs)
            costs.remove(min(costs))
            k = k-1
        return ans