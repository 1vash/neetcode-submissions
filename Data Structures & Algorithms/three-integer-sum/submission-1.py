from typing import List

class Solution:

    def twoSum_II_hashmap(self, nums, start, target):
        """Find all unique pairs in nums[start:] that sum up to target. 
        P.S The single start can generated multiple pairs e.g(3 and 5 = 8 and 2 and 6 = 8) and it's all results!
        - Uses a hashmap to store seen values for quick lookup.
        - Returns pairs of indices that form a valid sum.
        """
        h = {}  # Hashmap to store {value: index}
        pairs = set()
        
        for i in range(start, len(nums)):
            complement = target - nums[i]  # The number needed to form the target sum
            if complement in h:
                pairs.add((h[complement], i))  # Store indices as a pair (first index, second index)
            h[nums[i]] = i  # Store the current number's index for future lookup
        
        return pairs

    def twoSum_II_two_pointers(self, nums, start, target):
        """Find all unique pairs in nums[start:] that sum up to target."""
        pairs = set()
        l, r = start, len(nums) - 1
        while l < r:
            _sum = nums[l] + nums[r]
            if _sum > target:
                r -= 1
            elif _sum < target:
                l += 1
            else:
                pairs.add((l, r))
                # Skip duplicate values for l (optional)
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                # Skip duplicate values for r (optional)
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
        return pairs
            
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """Finds all unique triplets in nums that sum up to zero.
        - Sorts the array to make duplicate handling easier.
        - Iterates over each element, using it as a 'mid' element.
        - Calls twoSum to find pairs that complete the triplet.

        Two Sum HashMap for each Middle Value: T: O(N^2), S: O(N)
        Two Sum Two Pointers for each Middle Value: T: O(N^2), S: O(1)
        """
        TWO_POINTERS_TWO_SUM = True
        
        if TWO_POINTERS_TWO_SUM:
            #  Sorting ensures triplets are generated in a consistent order, avoiding duplicates 
            # and allow using two-pointer's approach
            nums.sort()
        else:
            # Sorting ensures triplets are generated in a consistent order, avoiding duplicates 
            # Note: Sorting is required even for HashMap solution as helpf with a consistent order!
            nums.sort()

        res = set()
        
        for mid_idx in range(len(nums)):
            # Skip duplicate mid elements to prevent redundant triplets (optional)
            if mid_idx > 0 and nums[mid_idx] == nums[mid_idx - 1]:
                continue  
            
            target = -nums[mid_idx]  # The sum we want from two other numbers

            if TWO_POINTERS_TWO_SUM:
                pairs = self.twoSum_II_two_pointers(nums, mid_idx + 1, target)
            else:
                pairs = self.twoSum_II_hashmap(nums, mid_idx + 1, target)
            
            for i, j in pairs:
                triplet = [nums[mid_idx], nums[i], nums[j]]  # Form the triplet
                res.add(tuple(triplet))  # Convert to tuple (hashable) to store in a set
        
        return [list(t) for t in res]  # Convert set of tuples back to a list of lists