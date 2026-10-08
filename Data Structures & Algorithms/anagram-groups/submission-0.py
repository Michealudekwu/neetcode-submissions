class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = []
        anagrams = {}
        for i in strs:
            keys.append("".join(sorted(i)))
        
        for i in range(len(strs)):
            if keys[i] not in anagrams:
                anagrams[keys[i]] = []

            anagrams[keys[i]].append(strs[i])

        return list(anagrams.values())