class Solution {
    public int solution(int order) {
        String strOrder = Integer.toString(order);
        int clapCount = 0;

        for (char c : strOrder.toCharArray()) {
            if (c == '3' || c == '6' || c == '9') {
                clapCount++;
            }
        }

        return clapCount;
    }
}
