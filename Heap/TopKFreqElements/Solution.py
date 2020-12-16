import heapq


class Solution:
    def top_K_frequent(self, nums: list, k: int) -> list:
        freq_dict = {}
        for n in nums:
            if n not in freq_dict:
                freq_dict[n] = 1
            else:
                freq_dict[n] += 1
        k_freq_elems = heapq.nlargest(k, freq_dict.items(), key=lambda x: x[1])
        return [key_freq_pair[0] for key_freq_pair in k_freq_elems]
