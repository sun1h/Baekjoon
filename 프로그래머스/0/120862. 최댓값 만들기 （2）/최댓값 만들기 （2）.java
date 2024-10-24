class Solution {
    public int solution(int[] numbers) {
        int answer =  Integer.MIN_VALUE; 
        for (int i = 0; i < numbers.length - 1; i++) {
            for (int j = i + 1; j < numbers.length; j++) {
                answer = findMax(answer, numbers[i], numbers[j]); // answer 업데이트
            }
        }
        return answer;
    }
    
    public int findMax(int currentMax, int num1, int num2) {
        int mul = num1 * num2;
        if (mul > currentMax) {
            return mul; // 최대값 반환
        }
        return currentMax; // 최대값 유지
    }
}
