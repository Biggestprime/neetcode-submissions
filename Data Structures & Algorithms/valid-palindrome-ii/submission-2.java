class Solution {
    public boolean validPalindrome(String s) {
        int l=0, r= s.length() - 1;
        return isPalindrom(s, l, r, false);
    }

    private boolean isPalindrom(String s, int l, int r, boolean deletedOnce) {
        while(l < r) {
            if(s.charAt(l) == s.charAt(r)) {
                l++;r--;
            }
            else if(deletedOnce) {
                return false;
            }
            else {
                return isPalindrom(s, l+1, r, true) 
                || isPalindrom(s, l, r - 1, true);
            }
        }

        return true;
    }
}


/**
Try recursive method

0 1 2 3 4 5

1 5
2 4
3

0 4
1 3
2


abdbcbda


***/