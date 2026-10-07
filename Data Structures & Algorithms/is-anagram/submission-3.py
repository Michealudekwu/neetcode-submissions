class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_dict_a = {}
        hash_dict_b = {}

        for c in s:
            hash_dict_a[c] = hash_dict_a.get(c, 0) + 1
        for c in t:
            hash_dict_b[c] = hash_dict_b.get(c, 0) + 1

        return hash_dict_a == hash_dict_b
        