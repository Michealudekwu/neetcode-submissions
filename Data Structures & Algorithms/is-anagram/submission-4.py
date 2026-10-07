class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_dict = {}

        for c in s:
            hash_dict[c] = hash_dict.get(c, 0) + 1
        for c in t:
            hash_dict[c] = hash_dict.get(c, 0) - 1

        return all(v == 0 for v in hash_dict.values())
        