class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mer_arr = nums1 + nums2
        mer_arr.sort()

        n = len(mer_arr)

        if n % 2 == 0:
            mid = n // 2
            return (mer_arr[mid - 1] + mer_arr[mid]) / 2
        else:
            return mer_arr[n // 2]