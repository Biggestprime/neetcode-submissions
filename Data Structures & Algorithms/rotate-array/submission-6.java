class Solution {
    public void rotate(int[] nums, int k) {

        List<Integer> rotatedElements = new ArrayList<>();
        while(k > nums.length) {
            k-=nums.length;
        }

        for(int i = nums.length - k;i<nums.length;i++) {
            rotatedElements.add(nums[i]);
        }

        //shift
        int l = nums.length - k - 1;
        int r = nums.length - 1;

        while(l>=0) {
            nums[r] = nums[l];
            l--;
            r--;
        }

        for(int i = 0; i < k; i++) {
            nums[i] = rotatedElements.get(i);
        }
    }

    /**
    extra memory O(n)

1 2 3 4

    **/
}