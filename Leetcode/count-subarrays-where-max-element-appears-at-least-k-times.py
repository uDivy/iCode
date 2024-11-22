class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        start = 0
        max_element = max(nums)
        count = 0
        subarray_count = 0

        for end in range(len(nums)):
            curr = nums[end]
            if curr == max_element:
                count += 1

            while count == k:
                if nums[start] == max_element:
                    count -= 1
                start += 1

            
            subarray_count += start 

        return subarray_count