class Solution {
    public String mergeAlternately(String word1, String word2) {
        int p1 = 0, p2 = 0;
        StringBuilder result = new StringBuilder();
        while(p1 < word1.length() && p2 < word2.length()) {
            result.append(word1.charAt(p1));
            result.append(word2.charAt(p2));
            p1++;p2++;
        }

        if(p1 < word1.length()) {
            result.append(word1.substring(p1));
        }
        else if(p2 < word2.length()) {
            result.append(word2.substring(p2));
        }

        return result.toString();
    }
}