import numpy as np
class Solution_Raw:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)
        nums_square = np.array(nums) ** 2
        left = np.argmin(nums_square)
        right = left
        sorted_square_nums = []
        sorted_square_nums.append(nums_square[left])
        while (left > 0 and right < length-1):
            if (nums_square[left-1] < nums_square[right+1]):
                left -= 1
                sorted_square_nums.append(nums_square[left])
            else:
                right += 1
                sorted_square_nums.append(nums_square[right])

        if (left > 0):
            tmp = nums_square[:left]
            sorted_square_nums += list(tmp[::-1])
        elif (right < length-1):
            sorted_square_nums += list(nums_square[right+1:])

        return sorted_square_nums

class Solution_Refined:   # The head and tail pointers simplify the code
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums_square = [i ** 2 for i in nums]
        left = 0
        right = n - 1
        result = [0] * n
        for i in range(n-1, -1, -1):
            if (left == right):
                result[i] = nums_square[left]
                return result
            if (nums_square[left] > nums_square[right]):
                result[i] = nums_square[left]
                left += 1
            else:
                result[i] = nums_square[right]
                right -= 1







