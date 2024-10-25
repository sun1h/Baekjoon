class Solution {
    public int[] solution(long n) {
        String str = Long.toString(n);
        int num = str.length();
        int[] answer = new int[num];


        for (int i = 0; i < num; i++) {
            answer[i] = Character.getNumericValue(str.charAt(num - 1 - i)); 
        }

        return answer; 
    }
}
