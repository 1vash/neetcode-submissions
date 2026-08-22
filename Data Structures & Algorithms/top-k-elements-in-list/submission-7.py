import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # T: O(n log k); S: O(n+k)

        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        h = []
        # O(M) ~ M unique numbers
        for num in count.keys():
            # heappush to firstly work by counter - needed counter first in tuple
            freq = count[num]
            heapq.heappush(h, (freq, num)) # (counter, num) - O(log k)
            
            if len(h) > k:
                heapq.heappop(h) # O(1)

        return [num for freq, num in h]
