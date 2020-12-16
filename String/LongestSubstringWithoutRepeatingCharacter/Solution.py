class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        chars = set()
        left = right = 0
        length = 0
        while left < len(s) and right < len(s):
            if s[right] not in chars:
                chars.add(s[right])
                right += 1
            else:
                chars.discard(s[left])
                left += 1
            length = max(length, right - left)
        return length
