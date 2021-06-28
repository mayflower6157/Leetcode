class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        raw_arr = arr.copy()   # Assignment don't create a new list
        duplicated_arr = []
        for i in range(n):
            if (len(duplicated_arr) >= n):
                for j in range(i, n):
                    arr[j] = duplicated_arr[j]
                return
            if (raw_arr[i] != 0):
                duplicated_arr.append(raw_arr[i])
            else:
                duplicated_arr.append(0)
                duplicated_arr.append(0)
            arr[i] = duplicated_arr[i]

