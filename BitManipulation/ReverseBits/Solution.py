class Solution:
    def reverse_bits(self, n: int) -> int:
        num = 0
        power = 31
        while n > 0:
            # AND last bit in the given number and if it's a 1,
            # then add the current value at the current bit
            if n & 1 == 1:
                num += 2 ** power
            # shift n to the left by 1 to update the next bit we check
            n >>= 1
            power -= 1
        return num
