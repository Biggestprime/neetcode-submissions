class Solution {
    public void rotate(int[] nums, int k) {
        k %= nums.length;
        //first reverse whole array
        reverse(nums, 0, nums.length - 1);
        //revrse first half
        //reverse second half
        reverse(nums, 0, k - 1);
        reverse(nums, k, nums.length - 1);
    }

    private void reverse(int[] nums, int start, int end) {
        while(start < end) {
            int temp = nums[end];
            nums[end] = nums[start];
            nums[start] = temp;
            start++;end--;
        }
    }

    /**
    extra memory O(n)

1 2 3 4

1 2 3 4 5 | 6 7 8; k=3

8 7 6 | 5 4 3 2 1
6 7 8 | 1 2 3 4 5




    **/
}