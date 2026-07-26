class Solution {
    public int islandPerimeter(int[][] grid) {
        for(int i = 0; i< grid.length;i++) {
            for(int j = 0; j < grid[0].length; j++) {
                if(grid[i][j] == 1) {
                    return calc(i, j, grid);
                }
            }
        }

        return 0;
    }
    
    private int calc(int row, int col, int[][] grid) {
        grid[row][col] = -1;
        int countWaterSides = 0;

        int[] rr = {0, 0, 1, -1};
        int[] cc = {1, -1, 0, 0};

        for(int i = 0; i < 4;i++) {
            int newRow = row + rr[i];
            int newCol = col + cc[i];

            if(newRow >= 0 && newRow < grid.length && 
               newCol >=0 && newCol < grid[0].length) {
               
               if(grid[newRow][newCol] == 0) {
                countWaterSides += 1;
               }
               else if(grid[newRow][newCol] == 1) {
                countWaterSides += calc(newRow, newCol, grid);
               }
            }
            else {
                countWaterSides += 1;
            }
        }

        return countWaterSides;
    }
}
/**

6+8+4+6
**/