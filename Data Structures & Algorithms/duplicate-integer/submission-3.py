class Solution:
    def hasDuplicate1(self, nums: List[int]) -> bool:
        # T: O(N), S: O(N)
        hashSet = set()
        for num in nums:
            if num in hashSet:
                return True
            hashSet.add(num)
        return False

    def hasDuplicate(self, nums: List[int]) -> bool:
        # T: O(N^2), S: O(1)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

                
