class Solution:
    def is_palindrome(self, s: str) -> bool:
        alnum_characters = []
        for ch in s:
            if ch.isalnum():
                alnum_characters.append(ch)
        word = "".join(alnum_characters).lower()

        for i in range(len(word) // 2):
            if i == len(word) - 1 - i:
                return True
            if word[i] != word[len(word) - 1 - i]:
                return False
        return True
