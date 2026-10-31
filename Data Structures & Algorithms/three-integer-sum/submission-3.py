class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_ = sorted(nums)
        triples = []

        for i in range(len(nums_)):
            if i > 0 and nums_[i] == nums_[i - 1]:
                continue
            j = i + 1
            k = len(nums_) - 1
            target = -nums_[i]

            while j < k:
                if nums_[j] + nums_[k] == target:
                    triples.append([nums_[i], nums_[j], nums_[k]])
                    j += 1
                    k -= 1
                    while j < k and nums_[j] == nums_[j - 1]:
                        j += 1
                    while j < k and nums_[k] == nums_[k + 1]:
                        k -= 1
                elif nums_[j] + nums_[k] > target:
                    k -= 1
                elif nums_[j] + nums_[k] < target:
                    j += 1

        return triples