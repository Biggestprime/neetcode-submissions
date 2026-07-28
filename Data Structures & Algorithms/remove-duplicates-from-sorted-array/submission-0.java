class Solution {
    public int removeDuplicates(int[] nums) {
        int i = 0;
        while(i < nums.length) {
            int j = i + 1;
            while(j < nums.length && nums[j] == nums[i]) {
                j++;
            }

            if(j == nums.length || nums[i] >= nums[j]) {
                return i+1;
            }

            //shift elements
            int p = i +1;
            while(j < nums.length) {
                nums[p] = nums[j];
                p++;
                j++;
            }

            i++;
        }

        return i+1;
    }
}

/**

1 2 2 2 2 2 2 2

**/