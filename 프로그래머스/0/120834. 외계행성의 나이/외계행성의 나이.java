class Solution {
    public String solution(int age) {
        String answer = "";
        String strAge = Integer.toString(age);
        
        for(int i=0; i<strAge.length();i++){
            char ch = (char) ('a' + (strAge.charAt(i) - '0'));
            answer += ch;
        }
        return answer;
    }
}