class Solution {
    public int maxArea(int[] heights) {
        int l = 0, r = heights.length - 1;
        int result = 0;

        while(l < r) {
            result = Math.max(result, (r - l) * Math.min(heights[l], heights[r]));
            if(heights[l] < heights[r]) {
                l++;
            }
            else {
                r--;
            }
        }

        return result;
    }

    /**

    max (a) dec * b inc


    **/
}
