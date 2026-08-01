class Solution {
    public int trap(int[] height) {
        int total = 0;
        for(int i = 1; i < height.length - 1;i++) {
            int largestLeft = findLargest(height, 0, i - 1);
            int largestRight = findLargest(height, i + 1, height.length - 1);
            if(largestLeft > height[i] && largestRight > height[i]) {
                total += Math.min(largestLeft, largestRight) - height[i];
            }
        }

        return total;
    }

    private int findLargest(int[] height, int l, int r) {
        int max = 0;
        while(l<=r) {
            max = Math.max(max, height[l]);
            l++;
        }

        return max;
    }
}


/**
2 + 2 + 3 + 2
**/