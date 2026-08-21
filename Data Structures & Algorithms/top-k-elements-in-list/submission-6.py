import heapq

class Solution:
    # T: O(2N * log k)) where log k is heapush(); 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Because popping before pushing removes the smallest element without knowing whether the new one is better, so the heap loses correct top-k candidates.
        
        If the heap currently has the top-2 frequencies [(2,2), (3,1)] and the next number has frequency 1, popping before pushing removes (2,2) even though 1 is worse, causing you to lose a valid top-k element.
        """
        
        # T: O(N); S: O(N) the worst case where each number is unique
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        

        heap = [] # (freq,num) and it stores S: O(K) elements
        # O(M) ~ M is unique numbers
        for num in count.keys():         
            heapq.heappush(heap, (count[num], num)) # O(log k)

            if len(heap) > k:
                heapq.heappop(heap) # O(1)

        return [num for freq, num in heap]
