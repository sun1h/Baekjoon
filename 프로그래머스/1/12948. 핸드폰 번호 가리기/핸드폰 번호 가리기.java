class Solution {
    public String solution(String phone_number) {
        int num = phone_number.length()-4;
        String answer = "*".repeat(num)+phone_number.substring(num,phone_number.length());
        return answer;
    }
}