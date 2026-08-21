class Solution_1:
    # Iterate over each bits and sum to result
    # T: O(log N); S: O(1); 
    # More specifically, it's O(log n) in terms of the input value n, 
    # since the binary representation of n has ⌊log₂(n)⌋ + 1 bits
    def hammingWeight(self, n: int) -> int:
        res = 0
        for bit in bin(n)[2:]: # '0b1011'
            res += int(bit)
        return res

class Solution:
    # Iterate over each bits and sum to result
    # T: O(log N); S: O(1); 
    # More specifically, it's O(log n) in terms of the input value n, 
    # since the binary representation of n has ⌊log₂(n)⌋ + 1 bits
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            bit = n % 2
            res += bit
            n = n >> 1
        return res
    