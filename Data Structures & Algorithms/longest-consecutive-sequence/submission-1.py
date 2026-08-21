class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set()
        max_consq_seq = 0
        for n in nums:
            hashSet.add(n)

        for i in range(len(nums)):

            # check if the `n` is the beginning of the sequence / no leftover element
            if nums[i]-1 in hashSet:
                continue

            # then `n` is beginning of the sequence
            n = 0
            curr_seq_len = 0

            while True:
                # just iterate till the last found element in the set
                if (nums[i] + n) in hashSet:
                    curr_seq_len += 1
                    n += 1
                else:
                    break

            max_consq_seq = max(max_consq_seq, curr_seq_len)

        return max_consq_seq