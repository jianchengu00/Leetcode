class Solution:
    def num_decodings(self, s: str) -> int:
        # edge case always returns 0
        if s[0] == '0':
            return 0

        decodings = [None for i in range(len(s) + 1)]
        return self.opt(s, len(s), decodings)

    def opt(self, s, n, decodings) -> int:
        # base cases
        if n == 0 or n == 1:
            return 1
        if decodings[n] is not None:
            return decodings[n]

        count = 0
        # if the n-1 char is not a '0', then they can be encoded as their
        # own letter, so we get opt from that
        if s[n - 1] > '0':
            count = self.opt(s, n - 1, decodings)
            # if the n-2 char allows for the creation of a 2 digit num from 10-26,
        # then we can also get opt from that
        if s[n - 2] == '1' or (s[n - 2] == '2' and s[n - 1] < '7'):
            count += self.opt(s, n - 2, decodings)

        decodings[n] = count
        return decodings[n]
