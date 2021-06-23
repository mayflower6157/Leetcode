class Solution_Array:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutive = [0]       #corner case: no consecutive 1s
        flag = 0
        for i in range(len(nums)):
            if (nums[i] == 0):
                flag = 0
            elif (nums[i] == 1):
                if (flag == 0):
                    consecutive.append(1)
                else:
                    consecutive[-1] += 1
                flag = 1
            else:
                raise Exception("Type Error: Not binary")

        return max(consecutive)

class Solution_Count:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = nums[0]
        max_count = count
        for i in range(1, len(nums)):
            if (nums[i] == 0):
                if (count > max_count):
                    max_count = count
                count = 0
            elif (nums[i] == 1):
                count += 1
            else:
                raise Exception("Type Error: Not binary")

        if (count > max_count):
            max_count = count

        return max_count
