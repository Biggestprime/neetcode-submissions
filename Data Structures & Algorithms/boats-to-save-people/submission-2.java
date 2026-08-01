class Solution {
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);
        int l = 0, r= people.length - 1;
        int tempLimit = limit;
        int count = 0;
        while(l <= r) {
            
            tempLimit -= people[r];
            if(l == r) {
                count++;
                break;
            }

            r--;
            if(tempLimit - people[l] >=0) {
                tempLimit-=people[l];
                l++;
            }

            count++;
            tempLimit = limit;
        }

        return count;
    }

    
}

/**

1 2 4 5

1 2 2 3 3

3 3 4 5


**/