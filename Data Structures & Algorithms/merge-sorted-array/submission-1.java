class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int p1 = 0, p2 = 0, end = nums1.length - 1;

        int i = Math.max(0, nums1.length - nums2.length);

        while(i < nums1.length) {
            nums1[i] = Integer.MAX_VALUE;
            i++;
        }

        while(p2 < nums2.length) {
            while(nums2[p2] >= nums1[p1]) {
                p1++;
            }

            //shift nums1
            while(end > p1) {
                nums1[end] = nums1[end - 1];
                end--;
            }

            nums1[p1] = nums2[p2];
            end = nums1.length - 1;
            p1++;p2++;
        }
    }
}