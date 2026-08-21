from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums

        # Iterate over each value in list and count occurrences
        counter = {} # {1: 3, 2: 3, 3: 1}
        for n in nums: # [1,1,1,2,2,2,3]
            counter[n] = counter.get(n, 0) +1

        # Bucket Sort Trick using counted values as bucket indexes
        bucket = [[] for _ in range(len(nums)+1)]
        for i, v in counter.items():
            bucket[v].append(i)

        print(bucket) # [[], [3], [], [1, 2], [], [], [], []]

        res = []
        for i in range(len(bucket)-1,-1,-1):
            for v in bucket[i]:
                res.append(v)
                if len(res) == k: # [1, 2]
                    return res
