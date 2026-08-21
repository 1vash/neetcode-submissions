import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        # range search is from 1 ... max(piles)
        while l <= r:
            k = (l + r) // 2
            total_count_by_k = sum([math.ceil(pile / k) for pile in piles])            
            if total_count_by_k <= h:
                # if total_count_by_k less than h then it's a valid solution
                # update res and skip all ranges above as `we are seeking the minimum k to eat all bananas in h hours`
                res = min(res, k)
                r = k - 1
            else:
                # k is big for eaten all bananas, our guessed number is low and we need consider higher values
                l = k + 1
        return res
            