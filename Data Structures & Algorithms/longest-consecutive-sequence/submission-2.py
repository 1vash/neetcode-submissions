class Solution:
    # T: O(N); M: O(N)
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set()
        for num in nums:
            hashSet.add(num)

        longest_consq = 0

        for num in hashSet:

            # only expand if this is the start of a sequence
            if num - 1 not in hashSet:
                start = end = num

                # to find an end point
                while end in hashSet:
                    end += 1
                # and get back to existing value
                end = end - 1

                longest_consq = max(longest_consq, end - start + 1)

        return longest_consq
