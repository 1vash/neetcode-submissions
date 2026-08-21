class Solution:
    # T: O(N), S: O(N)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {} # num:idx
        for idx, num in enumerate(nums):
            # INCORRECT: diff = num - target; Solve here "num - x = target"
            # CORRECT: diff = target - num; Solve here "num + x = target"
            diff = target - num
            if diff in h:
                return [h[diff], idx]
            h[num] = idx