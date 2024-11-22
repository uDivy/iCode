class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        
        # Calculate left products
        for i in range(1, n):
            output[i] = output[i - 1] * nums[i - 1]

        
        # Calculate right products and multiply with left products
        right_product = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]
        
        return output
        