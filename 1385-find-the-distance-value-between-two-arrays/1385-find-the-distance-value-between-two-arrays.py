class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        res = 0

        for x in arr1:
            k = bisect_left(arr2, x - d)
            if k == len(arr2) or arr2[k] > x + d:
                res += 1

        return res