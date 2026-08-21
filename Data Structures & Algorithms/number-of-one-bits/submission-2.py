class Solution_1:
    # Iterate over each bits and sum to result
    # T: O(log N) -> O(log 32) -> O(1) ; S: O(log 32); 
    # More specifically, it's O(log n) in terms of the input value n, 
    # since the binary representation of n has ⌊log₂(n)⌋ + 1 bits

    # We are guranteed to have 32 bits, so T: O(log N) -> O(log 32) -> O(1) 

    def hammingWeight(self, n: int) -> int:
        res = 0
        for bit in bin(n)[2:]: # '0b1011'
            res += int(bit)
        return res

class Solution_2:
    # Iterate over each bits and sum to result
    # T: O(log N) -> O(log 32) -> O(1) ; S: O(1); 
    # More specifically, it's O(log n) in terms of the input value n, 
    # since the binary representation of n has ⌊log₂(n)⌋ + 1 bits

    # We are guranteed to have 32 bits, so T: O(log N) -> O(log 32) -> O(1) 

    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            bit = n % 2
            res += bit
            n = n >> 1
        return res


"""
How it works:

ITERATION # 1
Original:        1 0 0 0 0 0 0 1
Subtract one:    0 0 0 0 0 0 0 1
Result:          1 0 0 0 0 0 0 0

Original:        1 0 0 0 0 0 0 1
& Result:        1 0 0 0 0 0 0 0
Result:          1 0 0 0 0 0 0 0

ITERATION # 2 ...
"""
    


class Solution:
    # Iterate over each bits and sum to result
    # T: O(log k) -> O(log 32) -> O(1) ; S: O(1); 
    # More specifically, it's O(log n) in terms of the input value n, 
    # since the binary representation of n has ⌊log₂(n)⌋ + 1 bits

    # We are guranteed to have 32 bits, so T: O(log N) -> O(log 32) -> O(1) 

    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n = n & (n-1)
            res += 1 
        return res
