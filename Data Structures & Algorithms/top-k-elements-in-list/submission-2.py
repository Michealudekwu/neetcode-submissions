from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict(int)
        freq_bucket = [[] for i in range(len(nums)+1)]
        k_nums = []

        for i in nums:
            hash_map[i] = hash_map.get(i, 0) + 1

        for num, freq in hash_map.items():
            freq_bucket[freq].append(num)

        for freqs in freq_bucket[::-1]:
            if freqs:
                for i in freqs:
                    if len(k_nums) >= k:
                        break
                    k_nums.append(i)
        # print(freq_bucket)
        # print(k_nums)
        return k_nums