class Solution:
    # Iterate over each bits and sum to result
    # T: O(N); S: O(1)
    def hammingWeight(self, n: int) -> int:
        res = 0
        for bit in bin(n)[2:]: # '0b1011'
            res += int(bit)
        return res