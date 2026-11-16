class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l, r = 0, 0
        seen = set()
        longest_count = 0

        while r < n:
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
                longest_count = max(longest_count, (r-l))
            else:
                seen.remove(s[l])
                l += 1

        return longest_count