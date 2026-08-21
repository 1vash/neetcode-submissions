class Solution:
    """
    T: O(N^2); S: O(n+m) (potentially O^2)
    nums[i] + nums[j] + nums[k] == 0
    -> nums[j] + nums[k] == -nums[i]

    Condition: i,j,k all distinct
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        
        for i, num in enumerate(nums):
            target = -nums[i]
            seen = {}
            for j in range(i + 1, len(nums)):
                complement = target - nums[j]
                if complement in seen:
                    triplet = tuple(sorted([nums[i], nums[j], complement]))
                    triplets.add(triplet)
                # record nums[j] as seen
                seen[nums[j]] = j
                
        return list(triplets)
            