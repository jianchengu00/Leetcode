class Solution:
    def hamming_weight(self, n: int) -> int:
        one_bits = 0
        while n > 0:
            if n & 1 == 1:
                one_bits += 1
            n >>= 1
        return one_bits
