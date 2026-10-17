class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product, zero_count = 1, 0
        n = len(nums)
        total = 0
        squars = []

        for num in nums:
            if num:
                product *= num
            else: 
                zero_count += 1

        if zero_count > 1:
            return [0] * n
        
        for num in nums:
            if zero_count:
                if num:
                    squars.append(0)
                else:
                    squars.append(product)
            else:
                squars.append(product // num)

        return squars 