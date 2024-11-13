from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        if len_nums1 <= len_nums2:
            smaller_array = nums1 
            larrger_array = nums2  
        else:
            smaller_array = nums2
            larrger_array = nums1 
        num_dict = {num: 1 for num in smaller_array}  # Create dictionary with keys as numbers and values as 1
        result = []  # Initialize result list
        for num in larrger_array:  # Iterate through the larger array
            if num in num_dict and num_dict[num] == 1:  # Check if the number is in num_dict and its value is 1
                result.append(num)  # Store the number in the result list
                num_dict[num] = 0  # Reduce the value to 0
        return result  # Return the result list
        