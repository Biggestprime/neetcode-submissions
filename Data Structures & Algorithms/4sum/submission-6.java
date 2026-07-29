class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        for(int i = 0; i < nums.length-2;i++) {
            if(i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            for(int j = i + 1; j < nums.length-1;j++) {
                if(j > i+1 && nums[j] == nums[j - 1]) {
                    continue;
                }

                for(int k = j + 1; k < nums.length;k++) {

                    if(k > j+1 && nums[k] == nums[k - 1]) {
                        continue;
                    }

                    long rem = (long) target - ((long) nums[i] + nums[j] + nums[k]);
                    if(rem > Integer.MAX_VALUE || rem < Integer.MIN_VALUE) {
                        continue;
                    }

                    int ind = Arrays.binarySearch(nums, k + 1, nums.length, (int)rem);
                    if(ind >= 0 && ind < nums.length) {
                        result.add(List.of(nums[i], nums[j], nums[k], (int)rem));
                    }
                }
            }
        }

        return result;
    }
}