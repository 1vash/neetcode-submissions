# from typing import List
#
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#
#         if len(nums) < 2:
#             raise ValueError('Not possible to have less than 2 elements in array')
#
#         print('Input:  ', nums)
#
#         prefix, postfix = [nums[0]], [nums[-1]]
#
#         # fill prefix arr
#         for i in range(1, len(nums)):
#             prefix.append(prefix[-1] * nums[i])
#
#         # fill postfix arr
#         for i in range(len(nums) - 2, -1, -1):
#             postfix.append(postfix[-1] * nums[i])
#
#             # reverse postfix, as we created it with help of .append()
#         postfix = postfix[::-1]
#
        # print('Prefix: ', prefix)
        # print('Postfix:', postfix)
#
#         # fill ans array except
#         ans = [0] * len(nums)
#         for i in range(len(nums)):
#             # fill corner cases, first and last values
#             if i == 0:
#                 ans[i] = postfix[i+1]
#             elif i == len(nums) - 1:
#                 ans[i] = prefix[i-1]
#             else:
#                 ans[i] = prefix[i - 1] * postfix[i + 1]
#
#         print('Result: ', ans)
#         return ans
#
# Solution().productExceptSelf(nums=[1,2,3,4])
# # Solution().productExceptSelf(nums = [-1,1,0,-3,3])
#

from typing import List

class Solution:
    """
    Input:   [1,  2,  4,  6]
    Prefix:  [1,  2,  8,  48]
    Postfix: [48, 48, 24, 6]
    Output:  [48, 24, 12, 8]

    Explanation:
    Take what is Left to `i-1` from Prefix
    Take from is Right to `i+1` from Postfix

    Output[0] = 48 -> Prefix[out_of_bounds=1 * Postfix[1]=48
    Output[1] = 24 -> Prefix[0]=1 * Postfix[2]=24
    Output[2] = 12 -> Prefix[1]=2 * Postfix[3]=6
    Output[3] = 8 -> Prefix[2]=8 * Postfix[out_of_bounds]=1
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if len(nums) < 2:
            raise ValueError('Not possible to have less than 2 elements in array')

        # print('Input:  ', nums)

        prefix_arr = [0] * len(nums)
        prefix_arr[0] = nums[0]

        postfix_arr = [0] * len(nums)
        postfix_arr[-1] = nums[-1]

        for i in range(1, len(nums)):
            prefix_arr[i] = nums[i] * prefix_arr[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            postfix_arr[i] = nums[i] * postfix_arr[i + 1]

        # print('Prefix: ', prefix_arr)
        # print('Postfix:', postfix_arr)

        # fill ans array except self
        ans = [0] * len(nums)
        for i in range(len(nums)):
            # fill corner cases
            if i == 0:
                ans[i] = postfix_arr[i+1]
            elif i == len(nums) - 1:
                ans[i] = prefix_arr[i-1]
            else:
                ans[i] = prefix_arr[i-1] * postfix_arr[i+1]

        # print('Result: ', ans)

        return ans


Solution().productExceptSelf(nums =  [1,2,4,6])