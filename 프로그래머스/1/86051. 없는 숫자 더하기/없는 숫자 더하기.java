import java.util.stream.*;

class Solution {
    public int solution(int[] numbers) {
        int answer = (1+9)*9/2 - IntStream.of(numbers).sum();
        
        return answer;
    }
}