class Solution:
    def group_anagrams(self, strs):
        # dict of unique anagram structures
        anagrams = {}
        # alphabet for making hashes
        alphabet = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8,
                    'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16,
                    'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

        for word in strs:
            num_chars = [0] * 26
            # use character occurrences in alphabetical order to generate a hash
            for ch in word:
                num_chars[alphabet[ch]] += 1

            hash_val = '#'.join(str(n) for n in num_chars)

            if hash_val not in anagrams:
                anagrams[hash_val] = [word]
            else:
                anagrams[hash_val].append(word)

        return anagrams.values()
