class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h = {}
        for n in nums:
            if n in h:
                return True
            h[n] = h.get(n, 0) + 1
        return False