from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seqs = defaultdict(int)
        nums = sorted(nums)
        count = []
        start = 0

        for i in nums:
            seqs[i] = seqs.get(i, 0) + 1

        for key, value in seqs.items():
            if (key-1) not in seqs:
                start = 0

            start += 1
            count.append(start)

        return max(count) if count else 0
