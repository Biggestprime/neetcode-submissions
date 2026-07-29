class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();

        for(int i = 0;i<nums.length;i++) {

            if(i > 0 && nums[i] == nums[i-1]) {
                continue;
            }//already processed with all pairs

            for(int j = i + 1; j < nums.length - 1;j++) {
                if(j > i +1 && nums[j] == nums[j - 1]) {
                    continue;
                }

                int rem = (nums[i] + nums[j]) * -1;

                int ind = Arrays.binarySearch(nums, j+1, nums.length, rem);

                if(ind >=0 && ind < nums.length) {
                    result.add(List.of(nums[i], nums[j], nums[ind]));
                }
            }
        }

        return result;
    }
}

/**

-4 -1 -1 0 1 2 

**/