class Solution:
    def count_substrings(self, s: str) -> int:
        num_palindromes = 0

        for i in range(len(s)):
            # palindromes can have a single char center, or double char center
            # account for both and continue to choose the max length one
            num_palindromes += self.expand(s, i, i)
            num_palindromes += self.expand(s, i, i + 1)

        return num_palindromes

    def expand(self, s, left, right):
        # given a center defined by left and right indices, we try to
        # expand the range by 1 on both sides and check if it's a palindrome
        num_expanded_palindromes = 0

        while left >= 0 and right < len(s) and s[left] == s[right]:
            num_expanded_palindromes += 1
            left -= 1
            right += 1

        return num_expanded_palindromes
