class Solution:
    """
    Prerequisits: WE MUST NOT BE ABLE TO SORT
    THIS IS THE 3RD SOLUTION ON LEETCODE.COM;

    Time Complexity: O(n2). We have outer and inner loops, each going through n elements.
    Space Complexity: O(n) for the hashset/hashmap.

    While the asymptotic complexity is the same, this algorithm is noticeably slower than the TWO POINTERS approach. 
    Lookups in a hashset, though requiring a constant time, are expensive compared to the direct memory access.

    nums[i] + nums[j] + nums[k] == 0
    -> nums[j] + nums[k] == -nums[i]

    Condition: i,j,k all distinct
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        
        for i, num in enumerate(nums):
            
            # target = nums[j] +nums[k] = −nums[i]
            # complement = nums[k] = −nums[i] − nums[j]
            target = -nums[i]

            seen = {}

            # note: start=i + 1 TO AVOID REUSING THE SAME INDICIES/VALUES 
            # e.g [15,1,0]; we can end up with i=15, j=15, k=15 in our result
            for j in range(i + 1, len(nums)): 
                # "nums[k] is a complement"
                complement = target - nums[j]
                if complement in seen:
                    triplet = tuple(sorted([nums[i], nums[j], complement]))
                    triplets.add(triplet)
                
                # record nums[j] as seen
                seen[nums[j]] = j
                
        return list(triplets)
            