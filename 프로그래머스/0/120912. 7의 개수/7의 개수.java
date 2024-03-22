class Solution {
    public int solution(int[] array) {
        int answer = 0;
        for(int i=0; i<array.length; i++){
            String number = Integer.toString(array[i]);
            answer += number.chars().filter(ch ->ch=='7').count();
        }
        return answer;
    }
}