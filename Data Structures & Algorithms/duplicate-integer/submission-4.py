class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # T: O(N), S: O(N); assuming the array is not sorting
        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False