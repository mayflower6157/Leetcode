class Solution_Head:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Only the first m elements of nums1 are needed. Besides, copy
        # method is optional here since the lengths of arrs are different
        raw_nums1 = nums1[:m].copy()
        point1 = point2 = 0

        for i in range(n+m):
            if (point1 == m):
                for j in range(i, n+m):
                    nums1[j] = nums2[point2]
                    point2 += 1
                return
            elif (point2 == n):
                for j in range(i, n+m):
                    nums1[j] = raw_nums1[point1]
                    point1 += 1
                return

            if (raw_nums1[point1] < nums2[point2]):
                nums1[i] = raw_nums1[point1]
                point1 += 1
            else:
                nums1[i] = nums2[point2]
                point2 += 1

class Solution_HeadSimplified:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Make a copy of the first m elements of nums1.
        nums1_copy = nums1[:m]

        # Read pointers for nums1Copy and nums2 respectively.
        p1 = 0
        p2 = 0

        # Compare elements from nums1Copy and nums2 and write the smallest to nums1.
        for p in range(n + m):
            # We also need to ensure that p1 and p2 aren't over the boundaries
            # of their respective arrays.
            if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
                nums1[p] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1

class Solution_Tail:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        point1 = m - 1
        point2 = n - 1

        for i in range(n+m-1, -1, -1):
            if (point2 < 0 or (point1 >= 0 and nums1[point1] > nums2[point2])):
                nums1[i] = nums1[point1]
                point1 -= 1
            else:
                nums1[i] = nums2[point2]
                point2 -= 1
