class Solution {
    public String solution(String phone_number) {
        int le = phone_number.length();
        String answer = "*".repeat(le-4);
        answer += phone_number.substring(le-4,le);
 
        return answer;
    }
}