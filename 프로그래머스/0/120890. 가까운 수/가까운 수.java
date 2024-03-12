class Solution {
    public int solution(int[] array, int n) {
        int answer = 0;
        int tmp = 200;
        for (int i = 0; i < array.length; i++) {
            int diff = Math.abs(array[i] - n);
            if (diff < tmp || (diff == tmp && array[i] < answer)) {
                answer = array[i];
                tmp = diff; 
            }
        }
        return answer;
    }
}
