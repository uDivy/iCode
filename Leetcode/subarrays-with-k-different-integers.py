class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        hashmap = {}
        start = 0
        subarrayCount = 0
        prefixElement = 0

        for end in range(len(nums)):
            curr = nums[end]
            hashmap[curr] = hashmap.get(curr, 0) + 1

            if len(hashmap) == k + 1:
                hashmap[nums[start]] -= 1
                if hashmap[nums[start]] == 0:
                    del hashmap[nums[start]]
                prefixElement = 0
                start += 1

            while hashmap.get(nums[start], 0) > 1:
                hashmap[nums[start]] -= 1
                prefixElement += 1
                start += 1

            if len(hashmap) == k:
                subarrayCount += (1 + prefixElement)

        return subarrayCount