class Solution_BruteForce:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length-1):
            remaining = target - nums[i]
            for j in range(i+1, length):
                if (nums[j] == remaining):
                    return [i, j]

        return []

class Solution_HashTable:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = dict()
        length = len(nums)
        for i in range(length):
            remaining = target - nums[i]
            if (remaining in hash_table.keys() and hash_table[remaining] != i):
                    return [i, hash_table[remaining]]
            else:
                hash_table[nums[i]] = i

        return []
