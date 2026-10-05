class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) < len(nums2):
            arr_a = nums1
            arr_b = nums2
        else:
            arr_a = nums2
            arr_b = nums1

        l, r = 0, len(arr_a) - 1
        total = len(arr_a) + len(arr_b)
        half = total // 2

        while True:
            i = (l + r) // 2
            j = half - i - 2

            a_left = arr_a[i] if i >= 0 else float("-infinity")
            a_right = arr_a[i + 1] if i + 1 < len(arr_a) else float("infinity")
            b_left = arr_b[j] if j >= 0 else float("-infinity")
            b_right = arr_b[j + 1] if j + 1 < len(arr_b) else float("infinity") 
            

            if a_left <= b_right and b_left <= a_right:
                # calculate median
                median = min(a_right, b_right)

                if total % 2 == 0:
                    median += max(a_left, b_left)
                    median /= 2
                return median
            elif a_left > b_right:
                r = i - 1
            else:
                l = i + 1             





            



            

                        

# 
#
#

 # 1 2, 3 at 1
 # 1 3, 2 4 at 1 2
 # l1 =0, mid1= 0, r1=1
 # l2 = 0, mid2 = 0, r2 =1
 # 1 4 7 8 | 4 4 5 6      
 # 1 2 3 4