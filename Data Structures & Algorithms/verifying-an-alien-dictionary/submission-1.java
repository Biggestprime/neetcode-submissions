class Solution {
    public boolean isAlienSorted(String[] words, String order) {
        Map<Character, Integer> orderingMap = new HashMap<>();
        for(int i = 0; i < order.length(); i++) {
            orderingMap.put(order.charAt(i), i);
        }

        for(int i = 0; i < words.length - 1; i++) {
            if(!checkOrder(words[i], words[i+1], orderingMap)) {
                return false;
            }
        }

        return true;
    }

    private boolean checkOrder(String first, String second, 
    Map<Character, Integer> orderingMap) {

        boolean isMatchPrefix = true;
        for(int i = 0; i < Math.min(first.length(), second.length());i++) {

            if(first.charAt(i) != second.charAt(i)) {
                isMatchPrefix = false;
            }

            if(orderingMap.get(second.charAt(i)) < orderingMap.get(first.charAt(i))) {
                return false;
            }
            else if(orderingMap.get(second.charAt(i)) > orderingMap.get(first.charAt(i))) {
                return true;
            }
        }

        if(isMatchPrefix) {
            return first.length() <= second.length();
        }

        return true;
    }
}