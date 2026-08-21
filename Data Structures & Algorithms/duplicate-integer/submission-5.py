class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # T: O(N*logN), S: O(1) or O(N) depending on the sorting algorithm
        
        # check the edge case
        if len(nums) <= 1:
            return False

        nums = sorted(nums)
        for i in range(1, len(nums)):
            j = i - 1
            if nums[i] == nums[j]:
                return True
        return False