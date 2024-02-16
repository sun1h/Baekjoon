class Solution {
    public int[] solution(long n) {
        String str = Long.toString(n);
        int[] answer = new int[str.length()];
        int index = 0;
        while(n > 0){
            answer[index++] = (int)(n % 10);
            n /= 10;
        }
        return answer;
    }
}
