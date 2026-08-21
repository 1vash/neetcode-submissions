class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # is array sorted? - Yes; but you should sort it by yourself
        # answer always exists - no, return None

        pairs = sorted((num, i) for i, num in enumerate(nums))

        l, r = 0, len(pairs) - 1
        
        while l < r:
            s = pairs[l][0] + pairs[r][0]
            if s > target:
                r -= 1
            elif s < target:
                l += 1
            else:
                return sorted([pairs[l][1], pairs[r][1]])
        return None

        