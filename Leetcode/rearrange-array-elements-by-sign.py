from typing import List

def rearrangeArray(nums: List[int]) -> List[int]:
    # Create an empty array of the same size
    result = [0] * len(nums)
    
    pos_index = 0  # Pointer for placing positive numbers
    neg_index = 1  # Pointer for placing negative numbers

    # Iterate through the nums array
    for num in nums:
        if num > 0:
            result[pos_index] = num
            pos_index += 2  # Move to the next even index
        elif num < 0:
            result[neg_index] = num
            neg_index += 2  # Move to the next odd index

    return result
        