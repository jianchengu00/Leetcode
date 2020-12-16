class Solution:
    def longest_palindrome(self, s: str) -> str:
        start = end = 0

        for i in range(len(s)):
            # palindromes can have a single char center, or double char center
            # account for both and continue to choose the max length one
            length = max(self.expand(s, i, i), self.expand(s, i, i + 1))
            if length > end - start:
                start = i - int((length - 1) / 2)
                end = i + int(length / 2)

        return s[start:end + 1]

    def expand(self, s, left, right):
        # given a center defined by left and right indices, we try to
        # expand the range by 1 on both sides and check if it's a palindrome
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
