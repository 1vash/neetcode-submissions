class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums =       [1, 2,   4,  6 ]
        # prefix_pr =  [1, 2,   8,  48] # ORDER ->
        # postfix_pr =  [48, 48, 24, 6 ] # ORDER <-

        prefix_pr = [1] * len(nums)
        for i in range(len(nums)):
            prefix_pr[i] = (prefix_pr[i - 1] if i > 0 else 1) * nums[i]

        postfix_pr = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            postfix_pr[i] = (postfix_pr[i + 1] if i < len(nums) - 1 else 1) * nums[i]

        # print(prefix_pr)
        # print(postfix_pr)

        res = [0] * len(nums)
        for i in range(len(nums)):
            left = prefix_pr[i - 1] if i > 0 else 1
            right = postfix_pr[i + 1] if i < len(nums) - 1 else 1
            res[i] = left * right
        return res